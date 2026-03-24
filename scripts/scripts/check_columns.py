import pandas as pd
from pathlib import Path

df = pd.read_parquet("data/raw/london_roads.parquet")
print(df.columns.tolist())