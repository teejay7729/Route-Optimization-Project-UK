import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

INPUT = RAW_DIR / "london_roads.parquet"
OUTPUT = RAW_DIR / "london_roads_with_coords.parquet"

def main():
    print("Loading road network with GeoPandas...")
    df = gpd.read_parquet(INPUT)

    print("Extracting centroid coordinates...")
    df["lon"] = df.geometry.centroid.x
    df["lat"] = df.geometry.centroid.y

    print(f"Saving to: {OUTPUT}")
    df.to_parquet(OUTPUT)

    print("Done. Coordinates added successfully.")

if __name__ == "__main__":
    main()