# Automotive Data Acquisition and Cleaning

## Week 2 Internship Project

**Role:** Automotive Data Analysis Specialist  
**Platform:** YuvaIntern  
**Tools:** Python, Pandas, NumPy, Matplotlib, Jupyter Notebook

## Project Overview

This project demonstrates a practical workflow for acquiring, structuring, profiling, cleaning, and validating automotive industry data.

The working dataset contains automotive production, domestic sales, and export information across vehicle categories and financial years. The cleaned dataset is prepared for subsequent exploratory data analysis (EDA), visualization, and future predictive modelling.

## Objectives

- Identify and use reliable public automotive data sources.
- Structure automotive data for Python-based processing.
- Use Pandas and NumPy for data inspection and cleaning.
- Identify missing, duplicate, inconsistent, and logically invalid values.
- Apply transparent cleaning rules without inventing unsupported values.
- Produce a reusable cleaned dataset for further analysis.

## Data Source

The project report identifies the **Society of Indian Automobile Manufacturers (SIAM) Industry Trends** as the primary source for production, domestic sales, and export statistics.

Additional sources identified for validation or future expansion include:

- SIAM Annual Reports
- SIAM Statistical Services
- Ministry of Heavy Industries / Vahan data for future EV analysis

## Dataset Structure

The working dataset uses four fields:

| Field | Description |
|---|---|
| `Financial_Year` | Financial year such as FY2020-21 |
| `Vehicle_Category` | Automotive category |
| `Metric` | Production, Domestic Sales, or Exports |
| `Units` | Number of vehicles |

The Week 2 report describes a working dataset of **90 records and 4 columns**, representing 3 metrics × 5 vehicle categories × 6 financial years.

## Cleaning Workflow

1. Load the raw CSV file.
2. Inspect shape, data types, missing values, duplicates, and numeric statistics.
3. Standardize text columns by removing extra spaces.
4. Convert `Units` to numeric values.
5. Remove exact duplicate rows.
6. Detect negative vehicle-count values.
7. Convert logically invalid negative counts to `NaN` rather than inventing a replacement.
8. Validate the cleaned dataset.
9. Save the cleaned data as a separate CSV file.

## Missing Values

Missingness is measured before treatment. The project does not automatically replace unknown values with averages because this could introduce artificial automotive volumes.

If future modelling requires imputation, the method should be selected according to the variable and documented.

## Outlier Identification

The report uses the **Interquartile Range (IQR)** method:

```text
IQR = Q3 - Q1
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Outliers are treated as review flags rather than automatically deleted. Automotive categories can naturally have very different scales.

## Project Files

```text
automotive-data-acquisition-cleaning/
│
├── README.md
├── automotive_cleaning.py
├── automotive_data_raw_week2.csv
├── automotive_data_cleaned_week2.csv
└── figures/
```

## How to Run

### 1. Install Python

Install Python 3.x and make sure Python is available in your terminal.

### 2. Install required libraries

```bash
pip install pandas numpy
```

### 3. Keep the files in the same folder

Place:

```text
automotive_cleaning.py
automotive_data_raw_week2.csv
```

in the same directory.

### 4. Run the script

```bash
python automotive_cleaning.py
```

The script creates:

```text
automotive_data_cleaned_week2.csv
```

## Validation

The script checks that:

- No negative `Units` values remain.
- No exact duplicate rows remain.
- Missing values are reported.
- The final dataset is saved separately from the raw dataset.

## Future Analysis

The cleaned dataset can support:

- Exploratory data analysis
- Year-on-year growth analysis
- Category-wise trend visualization
- Statistical analysis
- Predictive modelling
- Future EV data integration

## Key Learning

The project demonstrates that data cleaning requires both programming and domain understanding. An unusual value should be investigated before removal, and cleaning decisions should be documented so that the workflow remains reproducible and auditable.

## Author

**Samiksha Gurme**  
B.E. – Computer Science and Engineering  
Artificial Intelligence & Machine Learning  
Bheemanna Khandre Institute of Technology, Bhalki

## Internship

**YuvaIntern – Automotive Data Analysis Specialist**  
**Week 2 – Automotive Data Acquisition and Cleaning**
