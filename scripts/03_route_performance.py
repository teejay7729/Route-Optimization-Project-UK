import pandas as pd
from pathlib import Path

# -----------------------------
# Config
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

INPUT_PARQUET = PROCESSED_DIR / "synthetic_travel_times.parquet"
OUTPUT_PARQUET = PROCESSED_DIR / "route_performance.parquet"
OUTPUT_CSV = PROCESSED_DIR / "route_performance.csv"

# -----------------------------
# Helper: classify peak/off-peak
# -----------------------------
def classify_peak(hour):
    if 7 <= hour <= 9:
        return "morning_peak"
    if 16 <= hour <= 18:
        return "evening_peak"
    return "off_peak"

# -----------------------------
# Main
# -----------------------------
def main():
    print("Loading synthetic travel data...")
    df = pd.read_parquet(INPUT_PARQUET)

    print("Classifying peak/off-peak...")
    df["hour"] = df["timestamp"].dt.hour
    df["peak_period"] = df["hour"].apply(classify_peak)

    print("Aggregating route performance...")
    grouped = df.groupby("segment_id").agg(
        avg_speed_kmh=("speed_kmh", "mean"),
        avg_travel_time_s=("travel_time_seconds", "mean"),
        total_trips=("segment_id", "count"),
        highway=("highway", "first"),
        length_m=("length_m", "first")
    ).reset_index()

    print("Calculating congestion index...")
    grouped["congestion_index"] = grouped["avg_travel_time_s"] / grouped["length_m"]

    print(f"Saving Parquet to: {OUTPUT_PARQUET}")
    grouped.to_parquet(OUTPUT_PARQUET)

    print(f"Saving CSV to: {OUTPUT_CSV}")
    grouped.to_csv(OUTPUT_CSV, index=False)

    print("Done. Route performance table created.")

if __name__ == "__main__":
    main()