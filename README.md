# 📊 E-Commerce Customer Analytics Dashboard

An interactive Streamlit dashboard for analysing customer spending behaviour — with live filters, KPI cards, and charts — built on top of a full data cleaning and analysis pipeline.

---

## ✨ Features

- **Interactive sidebar filters** — filter all views by Education level and Marital Status in real time
- **KPI cards** — Total Spending, Average Spending, Average Income, and Customer Count update with every filter
- **3 charts** — Average Spending by Education, Average Spending by Marital Status, and a Spending Distribution histogram
- **Auto-insights** — highlights the highest-spending education group, marital status group, and highest-income group
- **Dataset preview** — expandable table showing the first 10 rows of filtered data
- **Full pipeline included** — `cleaning.py` + `analysis.py` generate the cleaned data and static charts before the dashboard runs

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- streamlit
- pandas
- matplotlib

```bash
pip install streamlit pandas matplotlib
```

### Step 1 — Clean the data

```bash
git clone https://github.com/Anas-Siddiqui-z5941/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard
python cleaning.py
```

Input: `data/marketing_campaign.csv`
Output: `data/cleaned_data.csv`

### Step 2 — (Optional) Run static analysis

```bash
python analysis.py
```

Output:
- `charts/` — 5 static PNG charts
- `business_report.md` — full Markdown business report

### Step 3 — Launch the dashboard

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## 📁 Project Structure

```
ecommerce-analytics-dashboard/
│
├── app.py                   # Streamlit dashboard (main entry point)
├── cleaning.py              # Data cleaning pipeline
├── analysis.py              # Static business analysis + chart generation
│
├── data/
│   ├── marketing_campaign.csv   # Raw input dataset
│   └── cleaned_data.csv         # Auto-generated cleaned output
│
├── charts/                  # Static PNG charts (from analysis.py)
│   ├── revenue_by_education.png
│   ├── revenue_by_marital_status.png
│   ├── spending_distribution.png
│   ├── education_distribution.png
│   └── response_by_education.png
│
├── business_report.md       # Auto-generated business analytics report
├── report.md                # Additional report
└── README.md
```

---

## 📊 Dashboard Sections

| Section | Description |
|---|---|
| **Key Metrics** | 4 KPI cards — total spend, avg spend, avg income, customer count |
| **Dataset Preview** | Expandable table with first 10 rows of filtered data |
| **Avg Spending by Education** | Bar chart broken down by education level |
| **Avg Spending by Marital Status** | Bar chart broken down by marital status |
| **Spending Distribution** | Histogram showing how spending is spread across customers |
| **Insights** | Auto-highlighted best-performing groups |

---

## ⚙️ Pipeline Steps

| Step | Script | Description |
|---|---|---|
| 1 | `cleaning.py` | Loads raw CSV, fills nulls, removes duplicates, standardizes dates, fixes types |
| 2 | `analysis.py` | Computes revenue stats, segments customers, exports charts and report |
| 3 | `app.py` | Reads cleaned CSV and renders the interactive Streamlit dashboard |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)

---

## 👤 Author

**Anas Mohiuddin Siddiqui**
B.Tech CSE @ Integral University | Aspiring ML Engineer
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)
