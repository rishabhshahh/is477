# **Status Report – Milestone 3**

## **Project Title**
**Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data**

## **Team Members**
- **Rishabh Shah**
- **Atharva Awasthi**

---

## **1. Overview of Progress**

Since submitting our Project Plan, our team has made substantial progress on the data preparation phase of the project. We successfully collected, cleaned, and merged three datasets—Traffic, Weather, and Air Quality—focused on the City of Chicago.

We now have a fully combined dataset (`final_dataset.csv`) integrating all sources using consistent **date** and **location** fields. Our project notebook (`Project.ipynb`) includes data acquisition details, ethical handling explanations, cleaning steps, and integration logic.

Overall, we remain on schedule, and the foundational data engineering work for the project is complete.

---

## **2. Updates on Tasks from the Project Plan**

Below is a detailed update on each task originally outlined in our Project Plan, along with references to committed artifacts.

### **2.1 Dataset Acquisition – Completed**

We downloaded and prepared the following datasets:

1. **Chicago Air Pollution (Kaggle)**  
   https://www.kaggle.com/datasets/asjad99/chicago-air-pollution  
   Stored as: `AirQuality.csv`, `Air.csv`

2. **Chicago Traffic Tracker (Data.gov → Chicago Open Data)**  
   https://catalog.data.gov/dataset/chicago-traffic-tracker-historical-congestion-estimates-by-segment-2024-current  
   Stored as: `traffic.csv`, `traffic2.csv`

3. **Chicago Weather Dataset (Kaggle)**  
   https://www.kaggle.com/code/sheemazain/weather-dataset-2024/notebook  
   Stored as: `Weather.csv`

All acquisition steps and ethical considerations are documented in **Project.ipynb** under  
**“Data Sources + Acquisition Details + Ethical Handling.”**

---

### **2.2 Storage and Organization – Completed**

- All datasets stored in CSV format for transparency.
- Repository includes:
  - Raw datasets (`AirQuality.csv`, `Weather.csv`, `traffic.csv`)
  - Cleaned merged dataset (`final_dataset.csv`)
- File naming conventions and structure documented in `ProjectPlan.md` and `Project.ipynb`.

---

### **2.3 Extraction & Enrichment – Completed**

We enriched the original datasets by:

- Standardizing date formats across all sources  
- Creating unified location fields for merging  
- Normalizing weather and traffic values  
- Selecting only relevant variables for final integration  

Processing steps are included in **Project.ipynb**.

---

### **2.4 Data Cleaning – Completed (Documentation In Progress)**

Cleaning tasks accomplished:

- Parsed and formatted dates
- Standardized column names (lowercase, underscores)
- Removed duplicates
- Addressed missing values by either removal or forward fill
- Ensured matching locations across datasets

Formal documentation (Module 10 requirement) is still being written.

---

### **2.5 Data Integration – Completed**

We merged all datasets using:

- **date**
- **location**

Resulting file: **`final_dataset.csv`**  
Integration logic is fully implemented in the notebook.

---

### **2.6 Ethical Data Handling – Completed**

- All datasets originate from public sources (Kaggle, Data.gov, Chicago Open Data).
- No personal or sensitive information is included.
- Usage follows all licensing terms (Kaggle open use, ODC PDDL).
- Ethical reasoning documented in **Project.ipynb**.

---

### **2.7 Workflow Automation – Not Started**

Planned task:  
Create a Snakemake workflow automating the steps:

1. Data loading  
2. Cleaning  
3. Integration  
4. Analysis + Visualization  

This will be developed for Milestone 4.

---

### **2.8 Data Quality Assessment – Not Started**

We will create a full profiling report (missing values, ranges, duplicates, limitations) by Nov 25.

---

### **2.9 Metadata & Documentation – Not Started**

Pending items:

- Data dictionary  
- Metadata following DataCite schema  
- Detailed README reproduction steps  

---

## **3. Updated Timeline**

| Task                                | Status          | Expected Completion |
| ----------------------------------- | --------------- | ------------------- |
| Dataset acquisition                 | **Done**        | Completed           |
| Extraction & enrichment             | **Done**        | Completed           |
| Data cleaning                       | **Done**        | Completed           |
| Data cleaning documentation         | **In progress** | Nov 25              |
| Data integration                    | **Done**        | Completed           |
| Ethical data handling               | **Done**        | Completed           |
| Data quality assessment             | **Not started** | Nov 25              |
| Workflow automation (Snakemake)     | **Not started** | Dec 1               |
| Analysis + visualizations           | **Not started** | Dec 5               |
| Metadata + data dictionary          | **Not started** | Dec 3               |
| README final report                 | **Not started** | Dec 8               |
| Final GitHub release                | **Not started** | Dec 10              |

The project is progressing well and on track for completion.

---

## **4. Changes to the Project Plan**

### **4.1 Replaced Placeholder Names**
All roles now list actual team members rather than placeholders.

### **4.2 Added Direct Dataset URLs**
We incorporated full direct links to all three datasets in the updated Project Plan.

### **4.3 Integration Strategy Improved**
Originally debated integration keys; finalized **date + location**, which produced the most reliable merge.

### **4.4 Weather Dataset Selection Modified**
We initially considered multiple weather sources but kept only the Kaggle/Open-Meteo dataset for consistency.

No major structural changes were required.

---

## **5. Next Steps**

### **5.1 Data Quality Assessment**
- Perform profiling  
- Document quality issues  
- Generate `data_quality_report.md`

### **5.2 Cleaning Documentation**
- Export cleaning logic into a reusable Python script  
- Describe all operations applied

### **5.3 Workflow Automation**
- Build a Snakemake pipeline from acquisition → visualization  
- Add logs for provenance tracking

### **5.4 Reproducibility Package**
- Create `requirements.txt`  
- Write full reproduction steps in README  
- Document dataset acquisition steps  

### **5.5 Metadata & Data Dictionary**
- Define all dataset variables  
- Provide a DataCite-style metadata file

### **5.6 Analysis & Visualization**
- Explore relationships among traffic, weather, and air quality  
- Generate plots and insights  
- Add findings to the README

### **5.7 Box Folder Setup**
- Upload final dataset  
- Provide shareable link  
- Add path to `.gitignore`

### **5.8 Final Report (README.md)**
- Combine findings, methods, metadata, and workflow  
- Prepare for final release

---

## **6. Individual Contributions**

### **Rishabh Shah**
For this milestone, I created the StatusReport.md, updated the ProjectPlan.md after receiving TA feedback, and added the dataset acquisition, ethical data handling explanation, and documentation to the Project.ipynb notebook. I also reviewed the merged dataset, organized repository files, and outlined upcoming tasks for Milestone 4.

### **Atharva Awasthi**
For this milestone, I collected and prepared the three datasets used in the project, including traffic, weather, and air quality data. I performed initial cleaning, standardized the date and location fields, and created the combined dataset stored as final_dataset.csv. I also contributed to the development of the Project.ipynb notebook by implementing integration logic and testing different merging strategies across the datasets.
