# **Project Plan – Milestone 2 (Updated)**  
## **Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data**

---

## **1. Overview**

This project aims to build a small “smart city” data pipeline that combines traffic, weather, and air quality data for the City of Chicago. Our goal is to explore how traffic patterns relate to weather conditions and how both factors may influence daily air quality.

By integrating three different public datasets, cleaning them, and automating the workflow, our final product will demonstrate an end-to-end data curation process using the full data lifecycle: acquisition → storage → cleaning → integration → quality assessment → analysis → documentation.

---

## **2. Research Questions**

Our main questions are:

1. **How do traffic congestion levels relate to daily air quality measurements in Chicago?**  
2. **Do certain weather conditions (temperature, wind, humidity, precipitation) correlate with worse or better air quality levels?**  
3. **Can combining traffic + weather data help explain fluctuations in PM2.5 and AQI values?**  

These questions guide our integration, cleaning, and analysis steps.

---

## **3. Team Members & Roles**

### **Rishabh Shah**  
- Documentation lead (Project Plan, Status Report, Final README)  
- Ethical data handling documentation  
- Notebook preparation and cleaning overview  
- Repository organization and structure  

### **Atharva Awasthi**  
- Data acquisition and preparation  
- Cleaning + preprocessing datasets  
- Dataset integration (date + location)  
- Early analysis and testing merge strategies  

Both team members will contribute code and documentation across the project, and Git commit history will clearly show individual contributions.

---

## **4. Datasets**

We will use **three public datasets**, all related to the City of Chicago. Each dataset comes from a different source and provides unique information needed for our analysis.

### **4.1 Air Quality Dataset (Kaggle)**  
Daily pollutant data including PM2.5, CO, NO2, and Ozone.  
**URL:** https://www.kaggle.com/datasets/asjad99/chicago-air-pollution  
**Format:** CSV  
**Access Method:** Kaggle file download

### **4.2 Traffic Dataset (Chicago Data Portal / Data.gov)**  
Historical congestion estimates by road segment.  
**URL:**  
https://catalog.data.gov/dataset/chicago-traffic-tracker-historical-congestion-estimates-by-segment-2024-current  
**Format:** CSV  
**Access Method:** Chicago Open Data download

### **4.3 Weather Dataset (Kaggle / Open-Meteo Derived)**  
Daily temperature, humidity, wind, pressure, etc.  
**URL:**  
https://www.kaggle.com/code/sheemazain/weather-dataset-2024/notebook  
**Format:** CSV  
**Access Method:** Kaggle file download  

All datasets contain **date fields** and **city-level location fields**, allowing us to integrate them based on shared keys.

---

## **5. How the Project Meets Course Requirements**

### **5.1 Data Lifecycle (Module 1)**  
We follow the full data lifecycle model:  
Acquire → Store → Clean → Integrate → Assess Quality → Document → Analyze → Automate → Preserve.

### **5.2 Ethical Data Handling (Module 2)**  
- All datasets come from public open-data sources (Kaggle, Data.gov).  
- No personal, private, or sensitive information is included.  
- Data usage complies with open licensing (PDDL, Kaggle public license).  
- Ethical details will be documented in `Project.ipynb` and the final README.

### **5.3 Data Collection & Acquisition (Module 3)**  
- Three datasets from **three different, trustworthy data sources**  
- Different formats and access methods (Kaggle downloads vs. open-data portal)  
- Acquisition steps will be documented with instructions for reproducibility.

### **5.4 Storage & Organization (Modules 4–5)**  
- Using tabular file storage (CSV).  
- Files stored in the project root for clarity.  
- Consistent file naming conventions (snake_case).  
- Merged dataset saved as `final_dataset.csv`.

### **5.5 Extraction & Enrichment (Module 6)**  
- Normalize column names and formats  
- Standardize date formats  
- Harmonize location fields  
- Select and clean relevant variables for integration  

### **5.6 Data Integration (Modules 7–8)**  
- Join keys: **date** and **location**  
- Integration implemented in Python with pandas  
- Final dataset: `final_dataset.csv`

### **5.7 Data Quality (Module 9)**  
We will generate a `data_quality_report.md` including:  
- Missing value checks  
- Outlier detection  
- Range validation  
- Duplicate checks  

### **5.8 Data Cleaning (Module 10)**  
We will document:  
- Missing value handling  
- Date parsing  
- Column standardization  
- Filtering invalid records  

Cleaning logic lives in `Project.ipynb`.

### **5.9 Workflow Automation & Provenance (Modules 11–12)**  
We will build a **Snakemake workflow** that automates:  
1. Load raw data  
2. Clean & enrich  
3. Integrate datasets  
4. Run analysis and generate visualizations  

All steps will produce logs documenting provenance.

### **5.10 Reproducibility & Transparency (Module 13)**  
Final deliverables will include:  
- `requirements.txt`  
- Workflow instructions  
- Data acquisition steps  
- Box folder with final datasets  
- Clear README with reproduction steps  

### **5.11 Metadata & Data Documentation (Module 15)**  
We will create:

- **Data dictionary** describing all fields  
- **Metadata file** following DataCite recommendations  
- **Codebook** explaining units, variables, and sources  

---

## **6. Constraints**

- Weather dataset is pre-cleaned; some normalization needed.  
- Traffic dataset is large and may require filtering for performance.  
- Air quality data has partial missing values for certain pollutants.  
- Merging requires careful alignment of date formats.  

---

## **7. Gaps / Pending Questions**

- Which pollutant (PM2.5, NO2, or Ozone) will be the primary focus in analysis?  
- How many final visualizations should be included in the final report?  
- Whether to add simple modeling or keep analysis descriptive only.  

---

## **8. Timeline**

| Task | Assigned To | Status | Due Date |
|------|-------------|--------|----------|
| Dataset acquisition | Atharva | Completed | Oct 10 |
| Cleaning & enrichment | Atharva | Completed | Oct 20 |
| Data integration | Atharva | Completed | Oct 22 |
| Ethical handling documentation | Rishabh | Completed | Oct 25 |
| Data quality assessment | Both | Not started | Nov 25 |
| Cleaning documentation | Rishabh | In progress | Nov 25 |
| Workflow automation (Snakemake) | Both | Not started | Dec 1 |
| Analysis & visualizations | Both | Not started | Dec 5 |
| Metadata + data dictionary | Rishabh | Not started | Dec 3 |
| Final README report | Rishabh | Not started | Dec 8 |
| Final GitHub Release | Both | Not started | Dec 10 |

The plan remains realistic and aligned with course deadlines.

---

## **9. Submission & Versioning Plan**

- All work will be committed through Git with clear commit messages.  
- Each team member will commit their own contribution summaries.  
- Milestone releases will be tagged:  
  - `project-plan`  
  - `status-report`  
  - `final-project`  

The final release will include all artifacts: datasets, workflows, metadata, analysis, and documentation.
