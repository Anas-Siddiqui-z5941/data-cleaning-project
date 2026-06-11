# 🧹 Data Cleaning Pipeline

A reusable Python data cleaning pipeline that processes raw CSV datasets — handling missing values, removing duplicates, standardizing formats, and fixing data types — then exports a clean, analysis-ready CSV.

---

## ✨ Features

- **Missing value handling** — fills numeric columns with mean, categorical columns with mode
- **Duplicate removal** — drops all duplicate rows automatically
- **Date standardization** — converts date columns to consistent `YYYY-MM-DD` format
- **Data type fixing** — converts age and numeric columns to correct types
- **Clean export** — saves processed data to a new CSV file ready for analysis

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pandas library

```bash
pip install pandas
```

### Run the pipeline

```bash
git clone https://github.com/Anas-Siddiqui-z5941/data-cleaning-project.git
cd data-cleaning-project
python main.py
```

Input: `data/marketing_campaign.csv`
Output: `data/cleaned_data.csv`

---

## 📁 Project Structure

```
data-cleaning-project/
│
├── main.py          # Entry point — runs the full cleaning pipeline
├── data/
│   ├── marketing_campaign.csv   # Raw input dataset
│   └── cleaned_data.csv         # Auto-generated cleaned output
└── README.md
```

---

## ⚙️ Pipeline Steps

| Step | Function | Description |
|---|---|---|
| 1 | `load_dataset()` | Loads raw CSV into a pandas DataFrame |
| 2 | `handle_missing_values()` | Fills nulls with mean (numeric) or mode (categorical) |
| 3 | `remove_duplicates()` | Drops duplicate rows |
| 4 | `standardize_formats()` | Converts date column to YYYY-MM-DD |
| 5 | `fix_data_types()` | Converts age column to integer |
| 6 | `save_cleaned_data()` | Exports cleaned DataFrame to CSV |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

---

## 👤 Author

**Anas Mohiuddin Siddiqui**  
B.Tech CSE @ Integral University | Aspiring ML Engineer  
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)