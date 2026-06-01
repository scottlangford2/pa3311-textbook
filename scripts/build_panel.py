#!/usr/bin/env python3
"""Build TX_City_Sales_Panel_2013_2024.{csv,xlsx} — annual city-year panel.

Long format, one row per city-year (2013-2024), all Texas cities.
Sources (all free, no API key):
  - TX Comptroller data.texas.gov: vfba-b57j (annual sales-tax allocation),
    7z4d-yf2c (taxable sales + business outlets, 2016+), 53pa-m7sm (sales-tax rate)
  - Census 2022 Census of Governments directory (county, metro flag, 2022 reference population)

Run from Datasets/:  python3 build_panel.py
Requires: pandas, requests, openpyxl, and _raw/cog2022.zip (from build_dataset.py).
"""
import io, os, zipfile, requests, pandas as pd

UA = {"User-Agent": "Mozilla/5.0"}
YEARS = (2013, 2024)
COG_ZIP = "_raw/cog2022.zip"
COG_URL = "https://www2.census.gov/programs-surveys/gov-finances/tables/2022/2022_Individual_Unit_File.zip"
norm = lambda s: str(s).upper().strip().replace(".", "").replace("  ", " ")

def soql(rid, params):
    r = requests.get(f"https://data.texas.gov/resource/{rid}.csv", params=params, headers=UA, timeout=300)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))

def clean_city(n):
    n = n.strip()
    for suf in (" CITY", " TOWN", " VILLAGE"):
        if n.endswith(suf):
            return n[:-len(suf)].strip()
    return n

# ---- 1. Annual sales-tax allocation (the panel backbone) ----
alloc = soql("vfba-b57j", {"$select": "city,report_year,sum(net_payment_this_period) as sales_tax_alloc",
             "$where": f"report_year>={YEARS[0]} and report_year<={YEARS[1]}",
             "$group": "city,report_year", "$limit": 50000})
alloc = alloc.rename(columns={"report_year": "year"})
alloc["key"] = alloc["city"].map(norm)

# ---- 2. Taxable sales (annual sum) + business outlets (avg of quarterly totals), 2016+ ----
q = soql("7z4d-yf2c", {"$select": "name,year,qtr,sum(taxable) as q_taxable,sum(outlets) as q_outlets",
         "$where": f"type='City' and year>=2016 and year<={YEARS[1]}",
         "$group": "name,year,qtr", "$limit": 50000})
ts = q.groupby(["name", "year"]).agg(taxable_sales=("q_taxable", "sum"),
                                      business_outlets=("q_outlets", "mean")).reset_index()
ts["business_outlets"] = ts["business_outlets"].round().astype("Int64")
ts["key"] = ts["name"].map(norm)
ts = ts.drop(columns=["name"])

# ---- 3. Sales-tax rate per city-year ----
rate = soql("53pa-m7sm", {"$select": "city,report_year,max(current_rate) as sales_tax_rate",
            "$where": f"report_year>={YEARS[0]} and report_year<={YEARS[1]}",
            "$group": "city,report_year", "$limit": 50000})
rate = rate.rename(columns={"report_year": "year"})
rate["key"] = rate["city"].map(norm)
rate = rate.drop(columns=["city"])

# ---- 4. Time-invariant attributes from Census 2022 directory ----
os.makedirs("_raw", exist_ok=True)
if not os.path.exists(COG_ZIP):
    open(COG_ZIP, "wb").write(requests.get(COG_URL, headers=UA, timeout=300).content)
with zipfile.ZipFile(COG_ZIP) as z:
    pid_lines = z.read([n for n in z.namelist() if "PID" in n][0]).decode("latin-1").splitlines()
rows = []
for ln in pid_lines:
    gid = ln[0:12]
    if gid[0:2] != "48" or gid[2:3] != "2":
        continue
    rows.append((clean_city(ln[12:76]), ln[76:111].strip().title(), pd.to_numeric(ln[116:125].strip(), errors="coerce")))
attr = pd.DataFrame(rows, columns=["city", "county", "population_2022_ref"])
attr["key"] = attr["city"].map(norm)
METRO = {"Harris","Dallas","Tarrant","Bexar","Travis","Collin","Denton","El Paso","Hidalgo","Fort Bend",
"Montgomery","Williamson","Cameron","Nueces","Brazoria","Bell","Galveston","Lubbock","Webb","Jefferson",
"Mclennan","Smith","Ellis","Hays","Comal","Guadalupe","Johnson","Parker","Kaufman","Rockwall","Ector",
"Midland","Taylor","Potter","Randall","Wichita","Brazos","Grayson","Tom Green"}
attr["metro_status"] = attr["county"].apply(lambda c: "Metro" if str(c).strip() in METRO else "Non-Metro")
attr = attr.drop(columns=["city"]).drop_duplicates("key")

# ---- 5. Assemble long panel ----
p = (alloc.merge(ts, on=["key", "year"], how="left")
          .merge(rate, on=["key", "year"], how="left")
          .merge(attr, on="key", how="left"))
p["sales_tax_alloc_per_capita"] = p["sales_tax_alloc"] / p["population_2022_ref"]
p["taxable_sales_per_capita"] = p["taxable_sales"] / p["population_2022_ref"]

cols = ["city", "county", "metro_status", "population_2022_ref", "year", "sales_tax_alloc",
        "sales_tax_alloc_per_capita", "taxable_sales", "taxable_sales_per_capita",
        "business_outlets", "sales_tax_rate"]
p = p[cols].sort_values(["city", "year"]).reset_index(drop=True)
p.to_csv("TX_City_Sales_Panel_2013_2024.csv", index=False)
with pd.ExcelWriter("TX_City_Sales_Panel_2013_2024.xlsx", engine="openpyxl") as xl:
    p.to_excel(xl, index=False, sheet_name="Panel")
print(f"Built panel: {len(p)} city-year rows, {p['city'].nunique()} cities, "
      f"years {p['year'].min()}-{p['year'].max()}, {len(cols)} columns.")
