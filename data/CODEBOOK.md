# PA 3311 / PS 3315 — Course Spine Datasets (Codebook)

Two related files. **Use the panel as the primary course dataset.**

| File | Shape | Has debt? | Best for |
|---|---|---|---|
| **`TX_City_Sales_Panel_2013_2024.xlsx`** ⭐ primary | long panel, city × year | no | trends, growth, paired/repeated comparisons, COVID shock, plus all cross-sectional methods on a single-year slice |
| `TX_City_Finance_2022.xlsx` supplement | cross-section, one row per city | **yes** | the regression/OVB module if you want a debt outcome (single year) |

---

## PRIMARY: `TX_City_Sales_Panel_2013_2024`
**Unit:** Texas city × year. **13,930 rows; 1,180 cities; years 2013–2024.** Long format (one row per city per year).

### Sources (all free, no API key)
- **Texas Comptroller, data.texas.gov** — Sales Tax Allocation (`vfba-b57j`, annual sum of monthly payments), Quarterly Sales Tax Historical (`7z4d-yf2c`, taxable sales + outlets, 2016+), City–County Comparison (`53pa-m7sm`, local rate).
- **Census 2022 Census of Governments directory** — `county`, `metro_status`, and a **2022 reference population** (time-invariant).

### Variables
| Variable | Description | Units | Notes |
|---|---|---|---|
| `city` | City name | — | |
| `county` | County | — | time-invariant |
| `metro_status` | Metro vs. Non-Metro | category | time-invariant; see note* |
| `population_2022_ref` | 2022 reference population | persons | **fixed across years** — denominator only |
| `year` | Calendar year | 2013–2024 | |
| `sales_tax_alloc` | Sales-tax allocation payments | $/yr | 2013–2024 |
| `sales_tax_alloc_per_capita` | alloc / 2022 ref population | $ | |
| `taxable_sales` | Total taxable sales | $/yr | **2016+ only** (blank 2013–15) |
| `taxable_sales_per_capita` | taxable_sales / 2022 ref population | $ | 2016+ |
| `business_outlets` | Avg. active business outlets (quarterly mean) | count | 2016+ |
| `sales_tax_rate` | Local sales-tax rate | percent | |

\* `metro_status` flags cities whose county is a major TX metro county (documented list in `build_panel.py`); a teaching simplification, not the full OMB delineation.

### Panel notes / teaching points
- **Mostly balanced:** 1,143 of 1,180 cities have all 12 years; the rest incorporated or began receiving allocations mid-period (unbalanced panel — a real teaching point).
- **`population_2022_ref` is fixed at 2022**, so per-capita values change only through the numerator. Free annual city population isn't available without the Census API; flagged as a deliberate simplification.
- **Taxable sales/outlets begin in 2016**, so 2013–2015 are blank for those columns.
- **2020 shows the COVID demand shock** in most cities — a great motivating example (e.g., Austin allocation dips 2019→2020 then surges).

### How this single file powers each module
- **Descriptives & graphs:** filter to one year (e.g., 2024) → skewed distributions of `sales_tax_alloc_per_capita`, histograms, mean vs. median, outliers.
- **z-scores & probability:** standardize per-capita sales tax within a year.
- **Hypothesis testing / CIs:** mean per-capita sales tax with a confidence interval (one year).
- **Independent-samples t-test:** per-capita sales tax for **Metro vs. Non-Metro** (one year).
- **Paired-samples t-test:** `sales_tax_alloc` **2019 vs. 2023** (or 2019 vs. 2020, COVID) — same cities, two years.
- **Correlation & simple regression:** `sales_tax_alloc` ~ `taxable_sales` (one year).
- **Multiple regression + OVB:** `sales_tax_alloc` ~ `business_outlets` (simple) → add `taxable_sales` (watch the coefficient move).
- **Trends/growth (panel bonus):** plot one city over time; compute year-over-year growth; compare metro vs. non-metro recovery after 2020.
- **Final project:** students pose their own question from the panel.

> In Excel, get a single-year cross-section with **Data → Filter** on `year`, or a **PivotTable**.

---

## SUPPLEMENT: `TX_City_Finance_2022` (has debt)
Cross-section, one row per city (N=1,202), 2022. Adds variables not available annually:
`property_tax`, `gen_sales_tax`, `total_taxes`, `tax_per_capita`, `lt_debt_os`, `st_debt_os`, `total_debt_os`, `debt_per_capita` — from the **U.S. Census 2022 Census of Governments** individual unit file (amounts in dollars; debt = long-term `49U` + short-term `64V`). Use this if you want a **debt** outcome for the regression/OVB module. **No fund balance** exists in any free source (so the literal Chapter 8 fund-balance variable can't be reproduced). ~30% of small cities carry $0 debt (real; good for discussing zeros/skew).

---
Built `2026-06-01`. Rebuild: `python3 build_panel.py` (primary) and `python3 build_dataset.py` (supplement). Both read `_raw/cog2022.zip`.
