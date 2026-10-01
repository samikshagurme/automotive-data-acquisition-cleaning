"""
Automotive Data Acquisition and Cleaning - Week 2
YuvaIntern | Automotive Data Analysis Specialist

This script profiles, cleans, validates and saves the automotive dataset.
Expected input:
    automotive_data_raw_week2.csv

Output:
    automotive_data_cleaned_week2.csv
"""

import pandas as pd
import numpy as np


RAW_FILE = "automotive_data_raw_week2.csv"
CLEAN_FILE = "automotive_data_cleaned_week2.csv"


def profile_data(df):
    """Print basic data-quality information before cleaning."""
    print("=== Initial Data Profiling ===")
    print("Shape:", df.shape)
    print("\nFirst five rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nNumeric summary:")
    print(df["Units"].describe())


def clean_data(df):
    """Apply the documented Week 2 cleaning rules."""
    text_cols = ["Financial_Year", "Vehicle_Category", "Metric"]

    # Standardize text fields
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].str.replace(r"\s+", " ", regex=True)

    # Convert Units to numeric; malformed values become NaN
    df["Units"] = pd.to_numeric(df["Units"], errors="coerce")

    # Remove exact duplicate records
    df = df.drop_duplicates()

    # Vehicle counts cannot logically be negative.
    # Do not invent a replacement value; convert invalid values to NaN.
    df.loc[df["Units"] < 0, "Units"] = np.nan

    return df


def validate_data(df):
    """Run final validation checks."""
    assert df["Units"].dropna().ge(0).all(), "Negative Units remain."
    assert df.duplicated().sum() == 0, "Duplicate rows remain."

    print("\n=== Final Validation ===")
    print("Shape:", df.shape)
    print("Missing values:")
    print(df.isna().sum())
    print("Duplicate rows:", df.duplicated().sum())
    print("Negative Units:", (df["Units"] < 0).sum())


def main():
    # Load raw data
    df = pd.read_csv(RAW_FILE)

    # Profile before cleaning
    profile_data(df)

    # Clean
    cleaned_df = clean_data(df)

    # Validate
    validate_data(cleaned_df)

    # Save clean dataset
    cleaned_df.to_csv(CLEAN_FILE, index=False)

    print(f"\nCleaned dataset saved as: {CLEAN_FILE}")


if __name__ == "__main__":
    main()
