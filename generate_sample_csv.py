
import pandas as pd
from pathlib import Path
import numpy as np

# Output folder for CSVs
DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)

# Buildings
buildings = ["Building1", "Building2"]

# Generate monthly timestamps for 2024
months = pd.date_range(start="2024-01-01", end="2024-12-01", freq="MS")  # MS = Month Start

for b in buildings:
    kwh_values = np.random.randint(200, 600, size=len(months))  # random monthly usage
    df = pd.DataFrame({
        "timestamp": months,
        "kwh": kwh_values
    })
    file_path = DATA_DIR / f"{b}.csv"
    df.to_csv(file_path, index=False)
    print(f"Generated {file_path}")
