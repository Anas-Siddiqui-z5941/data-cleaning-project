# 📋 Data Cleaning Report — Marketing Campaign Dataset

## Dataset Overview

| Property | Value |
|---|---|
| Dataset | Marketing Campaign |
| Raw rows | 2,240 |
| Cleaned rows | 2,240 |
| Total columns | 29 |
| Input file | `data/marketing_campaign.csv` |
| Output file | `data/cleaned_data.csv` |

---

## Cleaning Steps Applied

### 1. Missing Value Handling
- **Numeric columns** — filled with column mean
- **Categorical columns** — filled with column mode
- Columns checked: `Income`, `Year_Birth`, `Recency`, `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds`, and all purchase/campaign columns

### 2. Duplicate Removal
- Duplicates found: **0**
- All 2,240 rows were unique — no rows removed

### 3. Date Standardization
- Column: `Dt_Customer`
- Converted to consistent `YYYY-MM-DD` format using `pd.to_datetime()`

### 4. Data Type Fixing
- Numeric columns validated and cast to correct types
- Ensured no mixed-type columns remain in the cleaned output

---

## Column Summary

| Category | Columns |
|---|---|
| Customer info | `ID`, `Year_Birth`, `Education`, `Marital_Status`, `Income` |
| Household | `Kidhome`, `Teenhome` |
| Enrollment | `Dt_Customer`, `Recency` |
| Spending | `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds` |
| Purchases | `NumDealsPurchases`, `NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases`, `NumWebVisitsMonth` |
| Campaigns | `AcceptedCmp1–5`, `Response`, `Complain` |
| Internal | `Z_CostContact`, `Z_Revenue` |

---

## Summary

| Metric | Result |
|---|---|
| Total rows processed | 2,240 |
| Duplicates removed | 0 |
| Missing values filled | Yes (mean/mode imputation) |
| Date columns standardized | Yes (`Dt_Customer`) |
| Data types fixed | Yes |
| Output saved | `data/cleaned_data.csv` |

---

## Notes

- The dataset had no duplicate rows, indicating it was already deduplicated at source
- Missing values were imputed rather than dropped to preserve all 2,240 records
- The pipeline is reusable — swap the input CSV path in `main.py` to clean any similar dataset