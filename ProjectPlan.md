# Project Plan  
**Course:** Data Management and Integration  
**Team:** Rishabh Shah and Atharva Awasthi
**Project Title:** Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data  

---

## Overview  
Our project will build a simple, automated data pipeline that combines **traffic**, **weather**, and **pollution** data for a city such as Chicago or New York. By bringing these datasets together, we want to see how things like traffic volume and weather conditions affect air quality.  

The goal isn’t to create a complicated model but to show how data can be **collected, cleaned, integrated, and analyzed** in a clear, reproducible way. This project will also demonstrate good data management, ethical data use, and transparency.

---

## Research Questions  
1. How do traffic and weather patterns influence daily air quality?  
2. Can we find trends, such as which days or conditions tend to have the worst air quality?  
3. How can automation make data analysis and reporting easier for future city planners?

---

## Team and Roles  
- **[Your Name #1] – Data Collection and Integration**  
  - Finds and downloads the traffic, pollution, and weather data.  
  - Cleans and merges the data into one file.  
- **[Your Name #2] – Workflow and Documentation**  
  - Builds the workflow automation (using Python or Snakemake).  
  - Writes clear instructions and metadata so others can reproduce the results.  

Both team members will share writing and reporting tasks.

---

## Datasets  

### 1. City Open Data (Traffic and Air Quality)  
- **Source:** [Chicago Data Portal](https://data.cityofchicago.org/) or [NYC Open Data](https://opendata.cityofnewyork.us/)  
- **Access:** CSV download or API request  
- **What it includes:** Traffic flow, speed, crash counts, air quality readings (PM2.5, ozone, AQI).  
- **Why it matters:** Helps us see how human activity relates to air quality.  
- **License:** Publicly available for reuse (Open Data Commons).  

### 2. NOAA Weather Data  
- **Source:** [NOAA Climate Data Online API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)  
- **Access:** REST API using Python (`requests`)  
- **What it includes:** Daily temperature, wind speed, humidity, and precipitation.  
- **Why it matters:** Weather can influence pollution levels.  
- **License:** Public domain.  

**Integration Plan:**  
We’ll merge the datasets by **date** and **location** so each record shows one day’s weather, traffic, and air quality.

---

## Timeline  

| Week | Task | Who | Deliverable |
|------|------|-----|-------------|
| Sept 26 – Oct 7 | Form team and set up GitHub repo | All | Repository ready |
| Oct 7 – Oct 14 | Write and submit Project Plan | All | `ProjectPlan.md` + release |
| Oct 15 – Oct 25 | Collect and clean data | [Name #1] | `data_acquisition.py` |
| Oct 26 – Nov 5 | Merge datasets and check quality | [Name #1] | Integrated CSV |
| Nov 6 – Nov 11 | Write Status Report | All | `StatusReport.md` |
| Nov 12 – Nov 25 | Automate workflow and create visuals | [Name #2] | `Snakefile`, charts |
| Dec 4 – Dec 10 | Final report and GitHub release | All | `README.md` + final release |

---

## How This Meets Course Requirements  

### Data Lifecycle  
We’ll document every step from **collection → storage → integration → analysis → sharing**, so the workflow is clear and repeatable.  

### Ethical Data Use  
All data sources are public and contain no private information. We’ll follow each dataset’s license and credit the sources properly. We will make sure all data is from ethical sources and we will also cite authors that are credible as well. 

### Data Collection  
We’ll use simple Python scripts or API calls to download the data automatically. Each run will record when and where the data came from.  

### Storage and Organization  
Our project folder will look like this:
data/
raw/
cleaned/
integrated/
scripts/
acquisition/
integration/
analysis/

File names and small metadata notes (CSV + JSON) will be explained in the README.

### Extraction and Enrichment  
We’ll calculate new metrics like daily average temperature and categorize air quality levels (e.g., “Good,” “Moderate,” “Unhealthy”).  

### Integration  
We’ll merge the datasets by **date** and **city** using simple Pandas joins or SQL. This makes it fairly simple but keeping explanatory variables may be a little harder to calcualte.  

### Data Quality  
We’ll check for missing or duplicate entries and flag extreme or impossible values (like negative temperatures).  
Results will be summarized in a small `data_quality_report.md`.  

### Data Cleaning  
We’ll fill in missing values where possible and normalize measurements so they’re consistent across datasets.  

### Workflow Automation  
A **Snakemake** or **bash** script will run the entire process—from data download to cleaned output—automatically. We may also look into other python libraries that may be better and we may be more comfortable with (subprocess, plumbum, Airflow, etc). For now we will use Snakemake/bash and if we are unable to figure out we will pivot to python.  

### Reproducibility  
Anyone should be able to rerun the full workflow with a single command (`snakemake` or `bash run_all.sh`).  
We’ll include a `requirements.txt` file listing all software packages used.  

### Metadata and Documentation  
We’ll write a simple `data_dictionary.md` to explain each variable and its units.  
The README will include author names, licenses, and citations.

---

## Constraints  
- NOAA API has rate limits, so we may store data locally after one download.  
- Some cities might not have complete data for every day.  
- Large datasets could slow down analysis, so we’ll focus on smaller time ranges if needed.

---

## Gaps or Questions  
- We still need to pick the city (Chicago or NYC).  
- We’ll decide which pollution measure (PM2.5 or AQI) works best.  
- We may add simple charts instead of advanced modeling.  

---

## References  
- City of Chicago Data Portal – https://data.cityofchicago.org/  
- NOAA Climate Data API – https://www.ncdc.noaa.gov/cdo-web/webservices/v2  
- NYC Open Data – https://opendata.cityofnewyork.us/  
- Pandas Documentation – https://pandas.pydata.org/  
- Snakemake Workflow System – https://snakemake.readthedocs.io/  

---

*This document will be tagged and released under `project-plan` in the team GitHub repository for grading.*
