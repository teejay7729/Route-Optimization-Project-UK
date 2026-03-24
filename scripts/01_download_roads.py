import os
from pathlib import Path

import osmnx as ox
import pandas as pd

# -----------------------------
# Config
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

PLACE_NAME = "Greater London, United Kingdom"

OUTPUT_PARQUET = RAW_DIR / "london_roads.parquet"
OUTPUT_CSV = RAW_DIR / "london_roads.csv"

# -----------------------------
# Download road network
# -----------------------------
def main():
    print(f"Downloading road network for: {PLACE_NAME}")

    # Get drivable road network
    G = ox.graph_from_place(PLACE_NAME, network_type="drive")

    # Convert to GeoDataFrame (edges only)
    edges = ox.graph_to_gdfs(G, nodes=False)

    # Updated column names for OSMnx 2.x
    keep_cols = [
        "node_u",
        "node_v",
        "key",
        "highway",
        "length",
        "oneway",
        "geometry"
    ]

    existing_cols = [c for c in keep_cols if c in edges.columns]
    edges = edges[existing_cols].copy()

    # FIX: Convert highway lists to strings
    def normalize_highway(val):
        if isinstance(val, list):
            return ",".join(val)
        if pd.isna(val):
            return "unknown"
        return str(val)

    if "highway" in edges.columns:
        edges["highway"] = edges["highway"].apply(normalize_highway)

    # Save as Parquet
    print(f"Saving Parquet to: {OUTPUT_PARQUET}")
    edges.to_parquet(OUTPUT_PARQUET)

    # Save as CSV
    print(f"Saving CSV to: {OUTPUT_CSV}")
    edges.to_csv(OUTPUT_CSV, index=False)

    print("Done. Raw road network saved in data/raw/")

if __name__ == "__main__":
    main()