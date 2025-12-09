import pandas as pd
import numpy as np
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

input_file = project_root / "data" / "processed" / "final_dataset.csv"
output_dir = project_root / "data" / "cleaned"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "final_dataset_cleaned.csv"

df = pd.read_csv(input_file)

def clean_final_df(df):
    df = df.copy()

    df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce")

    text_cols = [
        "STREET", "DIRECTION", "FROM_STREET", "TO_STREET",
        "STREET_HEADING", "COMMENTS", "START_LOCATION", "END_LOCATION"
    ]
    for c in text_cols:
        if c in df.columns:
            df[c] = (
                df[c]
                .astype("string")
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

    for c in ["DIRECTION", "STREET_HEADING"]:
        if c in df.columns:
            df[c] = df[c].str.upper()
    df = df.dropna(subset=["No2"])
    numeric_cols = [
        "SPEED", "LENGTH", "BUS_COUNT", "MESSAGE_COUNT", "RECORD_ID",
        "START_LATITUDE", "START_LONGITUDE", "END_LATITUDE", "END_LONGITUDE",
        "TEMP", "PRCP", "HMDT", "WND_SPD", "ATM_PRESS",
        "Pm2.5", "Pm10", "No2", "So2", "Co", "Aqi"
    ]
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    if "SPEED" in df.columns:
        df.loc[(df["SPEED"] < 0) | (df["SPEED"] > 120), "SPEED"] = np.nan
    if "LENGTH" in df.columns:
        df.loc[df["LENGTH"] <= 0, "LENGTH"] = np.nan
    for c in ["BUS_COUNT", "MESSAGE_COUNT"]:
        if c in df.columns:
            df.loc[df[c] < 0, c] = np.nan

    for c in ["TEMP", "PRCP", "HMDT", "WND_SPD", "ATM_PRESS",
              "Pm2.5", "Pm10", "No2", "So2", "Co", "Aqi"]:
        if c in df.columns:
            df.loc[df[c] < 0, c] = np.nan

    if "SEGMENT_ID" in df.columns:
        df = df.drop_duplicates(subset=["TIME", "SEGMENT_ID"], keep="first")

    if "TIME" in df.columns:
        df["DATE"] = df["TIME"].dt.date
        df["YEAR"] = df["TIME"].dt.year
        df["MONTH"] = df["TIME"].dt.month
        df["DAY_OF_WEEK"] = df["TIME"].dt.day_name()
        df["HOUR"] = df["TIME"].dt.hour

    return df

final_df_cleaned = clean_final_df(df)

final_df_cleaned.to_csv(output_file, index=False)

print("dataset saved to:", output_file)
