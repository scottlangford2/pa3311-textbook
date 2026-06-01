#!/usr/bin/env python3
"""Rebuild TX_City_Finance_2022.{csv,xlsx} — the PA 3311 / PS 3315 spine dataset.

Sources (all free, no API key):
  - Census 2022 Census of Governments, Individual Unit File (population, taxes, debt)
    https://www2.census.gov/programs-surveys/gov-finances/tables/2022/2022_Individual_Unit_File.zip
  - Texas Comptroller data.texas.gov: vfba-b57j (sales-tax allocation),
    53pa-m7sm (rate), 7z4d-yf2c (taxable sales + outlets)

Run from the Datasets/ folder:  python3 build_dataset.py
Requires: pandas, requests, openpyxl. Re-downloads the Census zip to _raw/ if absent.
"""
import io, os, zipfile, requests, pandas as pd

UA = {"User-Agent": "Mozilla/5.0"}
RAW = "_raw"
COG_ZIP = f"{RAW}/cog2022.zip"
COG_URL = "https://www2.census.gov/programs-surveys/gov-finances/tables/2022/2022_Individual_Unit_File.zip"
norm = lambda s: str(s).upper().strip().replace(".", "").replace("  ", " ")

def soql(rid, params):
    r = requests.get(f"https://data.texas.gov/resource/{rid}.csv", params=params, headers=UA, timeout=180)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))

def clean_city(n):
    n = n.strip()
    for suf in (" CITY", " TOWN", " VILLAGE"):
        if n.endswith(suf):
            return n[:-len(suf)].strip()
    return n

# ---- Census finance (parse fixed-width straight from the zip) ----
os.makedirs(RAW, exist_ok=True)
if not os.path.exists(COG_ZIP):
    open(COG_ZIP, "wb").write(requests.get(COG_URL, headers=UA, timeout=300).content)
with zipfile.ZipFile(COG_ZIP) as z:
    pid_name = [n for n in z.namelist() if "PID" in n][0]
    dat_name = [n for n in z.namelist() if "DAT" in n][0]
    pid_lines = z.read(pid_name).decode("latin-1").splitlines()
    dat_lines = z.read(dat_name).decode("latin-1").splitlines()

rows = []
for ln in pid_lines:
    gid = ln[0:12]
    if gid[0:2] != "48" or gid[2:3] != "2":   # Texas, City
        continue
    rows.append((gid, clean_city(ln[12:76]), ln[76:111].strip().title(), ln[111:116].strip(), ln[116:125].strip()))
pid = pd.DataFrame(rows, columns=["gid", "city", "county", "place_fips", "population"])
pid["population"] = pd.to_numeric(pid["population"], errors="coerce")
tx = set(pid["gid"])

from collections import defaultdict
items = defaultdict(dict)
for ln in dat_lines:
    gid = ln[0:12]
    if gid not in tx:
        continue
    try:
        items[gid][ln[12:15]] = float(ln[15:27].strip()) * 1000.0  # thousands -> dollars
    except ValueError:
        pass

fin = []
for gid in pid["gid"]:
    d = items.get(gid, {})
    ltd, std = d.get("49U", 0.0), d.get("64V", 0.0)
    fin.append((gid, d.get("T01", 0.0), d.get("T09", 0.0),
                sum(v for c, v in d.items() if c.startswith("T")), ltd, std, ltd + std))
fin = pd.DataFrame(fin, columns=["gid", "property_tax", "gen_sales_tax", "total_taxes",
                                 "lt_debt_os", "st_debt_os", "total_debt_os"])
df = pid.merge(fin, on="gid")
df = df[df["population"] > 0].copy()
df["key"] = df["city"].map(norm)

# ---- Comptroller ----
alloc = []
for yr in (2019, 2023):
    a = soql("vfba-b57j", {"$select": "city,sum(net_payment_this_period) as v",
                           "$where": f"report_year={yr}", "$group": "city", "$limit": 5000})
    alloc.append(a.rename(columns={"v": f"sales_tax_alloc_{yr}"}))
alloc = alloc[0].merge(alloc[1], on="city", how="outer")
alloc["key"] = alloc["city"].map(norm)
alloc = alloc.drop(columns=["city"]).groupby("key", as_index=False).sum(numeric_only=True)

rate = soql("53pa-m7sm", {"$select": "city,current_rate", "$where": "report_year=2024",
                          "$group": "city,current_rate", "$limit": 6000})
rate["key"] = rate["city"].map(norm)
rate = rate.drop_duplicates("key")[["key", "current_rate"]].rename(columns={"current_rate": "sales_tax_rate"})

ts = soql("7z4d-yf2c", {"$select": "name,sum(taxable) as taxable_sales,sum(outlets) as business_outlets",
                        "$where": "type='City' AND year=2022", "$group": "name", "$limit": 6000})
ts["key"] = ts["name"].map(norm)
ts = ts.drop(columns=["name"]).groupby("key", as_index=False).sum(numeric_only=True)

m = df.merge(alloc, on="key", how="left").merge(rate, on="key", how="left").merge(ts, on="key", how="left")

# ---- derived + metro flag ----
m["tax_per_capita"] = m["total_taxes"] / m["population"]
m["debt_per_capita"] = m["total_debt_os"] / m["population"]
m["taxable_sales_per_capita"] = m["taxable_sales"] / m["population"]
m["salestax_growth_19_23_pct"] = (m["sales_tax_alloc_2023"] - m["sales_tax_alloc_2019"]) / m["sales_tax_alloc_2019"] * 100
METRO = {"Harris","Dallas","Tarrant","Bexar","Travis","Collin","Denton","El Paso","Hidalgo","Fort Bend",
"Montgomery","Williamson","Cameron","Nueces","Brazoria","Bell","Galveston","Lubbock","Webb","Jefferson",
"Mclennan","Smith","Ellis","Hays","Comal","Guadalupe","Johnson","Parker","Kaufman","Rockwall","Ector",
"Midland","Taylor","Potter","Randall","Wichita","Brazos","Grayson","Tom Green"}
m["metro_status"] = m["county"].apply(lambda c: "Metro" if str(c).strip() in METRO else "Non-Metro")

cols = ["city","county","place_fips","metro_status","population","property_tax","gen_sales_tax","total_taxes",
"tax_per_capita","lt_debt_os","st_debt_os","total_debt_os","debt_per_capita","sales_tax_rate","taxable_sales",
"taxable_sales_per_capita","business_outlets","sales_tax_alloc_2019","sales_tax_alloc_2023","salestax_growth_19_23_pct"]
m = m[cols].sort_values("population", ascending=False).reset_index(drop=True)
m.to_csv("TX_City_Finance_2022.csv", index=False)
with pd.ExcelWriter("TX_City_Finance_2022.xlsx", engine="openpyxl") as xl:
    m.to_excel(xl, index=False, sheet_name="TX Cities")
print(f"Built TX_City_Finance_2022.{{csv,xlsx}} — {len(m)} cities, {len(cols)} variables.")
