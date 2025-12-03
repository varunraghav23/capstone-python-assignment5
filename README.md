# campus-energy-dashboard-VARUN
# Energy Consumption Analysis — Capstone Project

## Objective
The goal of this project is to **analyze and visualize electricity consumption across multiple buildings**.  
We automatically load monthly usage data from multiple CSV files, aggregate and summarize the data, generate building-wise insights, and create a visual dashboard.  

Key objectives include:  
- Combine multiple CSV files into a single clean dataset.  
- Calculate monthly consumption totals and building-level summaries.  
- Model the problem using object-oriented programming for scalability.  
- Visualize trends, compare building usage, and detect peak consumption periods.  
- Export cleaned data and generate a concise executive report.

---

## Dataset Source
For this project, **synthetic monthly electricity usage data** was generated for 2 buildings over 6 months (January – June 2024).  
Each CSV file contains:  
- `timestamp`: start of the month  
- `kwh`: electricity consumption for the month  
- `building`: building name (added during data loading)

Files used:  
- `Building1.csv`  
- `Building2.csv`  

*Note: In a real-world scenario, these files would come from building energy meters or energy management systems.*

---

## Methodology
The analysis is divided into five key tasks:

### Task 1 — Data Loading & Merging
- Automatically detect all CSV files in the `data/` directory.  
- Load and combine them into a single Pandas DataFrame (`df_combined`).  
- Add metadata (building name) if missing.  

### Task 2 — Aggregation & Summarization
- Calculate **monthly totals** of energy consumption.  
- Generate **building-wise summary tables** (mean, min, max, total).  

### Task 3 — Object-Oriented Modeling
- Create `MeterReading` and `Building` classes to encapsulate readings and computations.  
- Use `BuildingManager` to manage multiple building objects.  

### Task 4 — Visualization
- Create a **dashboard** with:  
  1. Trend line — monthly consumption over time.  
  2. Bar chart — average monthly usage per building.  
  3. Scatter plot — individual monthly readings per building.  
- Save as `dashboard.png` in the `output/` directory.

### Task 5 — Persistence & Executive Summary
- Save cleaned combined dataset as `cleaned_energy_data.csv`.  
- Save building summary statistics as `building_summary.csv`.  
- Generate a short summary report (`summary.txt`) including:  
  - Total campus consumption  
  - Highest-consuming building  
  - Peak load time  

---

## Insights
Based on the generated dataset:  
- **Total campus consumption** over 6 months is summarized in `summary.txt`.  
- The **highest-consuming building** can be quickly identified from the summary table.  
- Monthly trends allow identification of peak and low usage months.  
- Visualizations provide an intuitive view of energy consumption patterns across buildings, helping in **energy planning and optimization**.  

---

## Output Files
- `output/cleaned_energy_data.csv` — combined dataset of all buildings  
- `output/building_summary.csv` — building-wise statistics  
- `output/summary.txt` — concise executive summary  
- `output/dashboard.png` — visual dashboard of consumption trends  

---

## Tools & Libraries
- Python 3.11  
- Pandas  
- Matplotlib  
- Pathlib  

