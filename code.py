import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

# -------------------------------
# Paths
# -------------------------------
DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# -------------------------------
# Task 1 — Load & Combine CSVs
# -------------------------------
def load_and_merge_csvs(folder: Path) -> pd.DataFrame:
    combined = []
    log = []

    for file in folder.glob("*.csv"):
        try:
            df = pd.read_csv(file, on_bad_lines="skip")

            if df.empty:
                log.append(f"Skipped empty file: {file.name}")
                continue

            # Add building name from file
            df["building"] = file.stem
            combined.append(df)

        except Exception as e:
            log.append(f"Error reading {file.name}: {e}")

    if not combined:
        raise ValueError("No usable CSV files found.")

    merged = pd.concat(combined, ignore_index=True)
    print("\n".join(log) if log else "All files loaded successfully.")
    return merged

df_combined = load_and_merge_csvs(DATA_DIR)

# Ensure timestamp is datetime and set as index
df_combined["timestamp"] = pd.to_datetime(df_combined["timestamp"])
df_combined = df_combined.set_index("timestamp").sort_index()

# -------------------------------
# Task 2 — Aggregation Functions
# -------------------------------
def calculate_monthly_totals(df):
    return df.resample("M")["kwh"].sum()

def building_wise_summary(df):
    return (
        df.groupby("building")["kwh"]
          .agg(["mean", "min", "max", "sum"])
          .rename(columns={"sum": "total"})
    )

monthly_totals = calculate_monthly_totals(df_combined)
summary_table = building_wise_summary(df_combined)

# -------------------------------
# Task 3 — Object-Oriented Model
# -------------------------------
class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading: MeterReading):
        self.readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return f"{self.name} — total consumption: {total} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, reading):
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(reading)

manager = BuildingManager()
for _, row in df_combined.reset_index().iterrows():
    manager.add_reading(row["building"], MeterReading(row["timestamp"], row["kwh"]))

# -------------------------------
# Task 4 — Visualization Dashboard
# -------------------------------
fig, axs = plt.subplots(3, 1, figsize=(12, 14))

# Trend line — Monthly consumption
monthly_totals.plot(ax=axs[0], marker="o", title="Monthly Consumption Trend")
axs[0].set_ylabel("kWh")

# Bar chart — Average monthly usage per building
summary_table["mean"].plot(kind="bar", ax=axs[1], title="Average Monthly Usage per Building")
axs[1].set_ylabel("kWh")

# Scatter plot — Individual readings
for b in df_combined["building"].unique():
    building_df = df_combined[df_combined["building"] == b]
    axs[2].scatter(building_df.index, building_df["kwh"], label=b, s=50)
axs[2].set_title("Monthly Consumption per Building")
axs[2].set_ylabel("kWh")
axs[2].set_xlabel("Time")
axs[2].legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "dashboard.png")
plt.close()

# -------------------------------
# Task 5 — Save Outputs & Summary
# -------------------------------
df_combined.to_csv(OUTPUT_DIR / "cleaned_energy_data.csv")
summary_table.to_csv(OUTPUT_DIR / "building_summary.csv")

total_campus = df_combined["kwh"].sum()
highest_building = summary_table["total"].idxmax()
peak_time = df_combined["kwh"].idxmax()

report = f"""
Energy Summary Report
------------------------------
Total campus consumption: {total_campus:.2f} kWh
Highest consuming building: {highest_building}
Peak load time: {peak_time}
"""

with open(OUTPUT_DIR / "summary.txt", "w") as f:
    f.write(report)

print(report)
