import pandas as pd
import numpy as np
from pathlib import Path
import random
from datetime import datetime, timedelta

# -----------------------------
# Config
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

INPUT_PARQUET = RAW_DIR / "london_roads.parquet"
OUTPUT_PARQUET = PROCESSED_DIR / "synthetic_travel_times.parquet"
OUTPUT_CSV = PROCESSED_DIR / "synthetic_travel_times.csv"

# -----------------------------
# Synthetic travel time generator
# -----------------------------
def generate_synthetic_data(edges, num_vehicles=50, trips_per_vehicle=200):
    rows = []

    # Create a unique segment ID for each road segment
    edges = edges.reset_index(drop=True)
    edges["segment_id"] = edges.index

    # Ensure highway is always a string
    def normalize_highway(val):
        if isinstance(val, list):
            return ",".join(val)
        if pd.isna(val):
            return "unknown"
        return str(val)

    if "highway" in edges.columns:
        edges["highway"] = edges["highway"].apply(normalize_highway)
    else:
        edges["highway"] = "unknown"

    for vehicle_id in range(1, num_vehicles + 1):
        current_time = datetime(2024, 1, 1, 6, 0, 0)

        for _ in range(trips_per_vehicle):
            row = edges.sample(1).iloc[0]

            # Base speed (km/h)
            base_speed = random.uniform(20, 50)

            # Rush hour slowdown
            if 7 <= current_time.hour <= 9 or 16 <= current_time.hour <= 18:
                base_speed *= random.uniform(0.4, 0.7)

            # Random heavy delay (5% chance)
            if random.random() < 0.05:
                base_speed *= random.uniform(0.2, 0.5)

            # Calculate travel time
            length_km = row["length"] / 1000
            travel_time_hours = length_km / (base_speed / 60)
            travel_time_seconds = travel_time_hours * 3600

            rows.append({
                "vehicle_id": vehicle_id,
                "timestamp": current_time,
                "segment_id": row["segment_id"],
                "highway": row["highway"],
                "length_m": row["length"],
                "speed_kmh": base_speed,
                "travel_time_seconds": travel_time_seconds
            })

            # Move time forward
            current_time += timedelta(seconds=travel_time_seconds)

    return pd.DataFrame(rows)

# -----------------------------
# Main
# -----------------------------
def main():
    print("Loading road network...")
    edges = pd.read_parquet(INPUT_PARQUET)

    print("Generating synthetic travel times...")
    df = generate_synthetic_data(edges)

    print(f"Saving Parquet to: {OUTPUT_PARQUET}")
    df.to_parquet(OUTPUT_PARQUET)

    print(f"Saving CSV to: {OUTPUT_CSV}")
    df.to_csv(OUTPUT_CSV, index=False)

    print("Done. Synthetic travel dataset created.")

if __name__ == "__main__":
    main()