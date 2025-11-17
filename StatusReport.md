# **Status Report – Milestone 3**

## **Project Title**

**Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data**

## **Team Members**

* **Rishabh Shah**
* **Atharva Awasthi**

---

## **1. Overview of Progress**

Since submitting our Project Plan, we have made strong progress on the core parts of our project. We successfully collected, cleaned, and merged three datasets (Traffic, Weather, and Air Quality), all focused on the City of Chicago. Our goal is to study how traffic levels and weather conditions relate to daily air quality.

We now have a fully combined dataset (`final_dataset.csv`) that integrates all sources using the shared fields **date** and **location**. We also developed our Python notebook (`Project.ipynb`) with data acquisition summaries, cleaning steps, and integration logic.

Overall, the project is on schedule, and we have completed the entire data preparation stage.

---

## **2. Updates on Tasks from the Project Plan**

Below is a status update for each task originally defined in our Project Plan, along with references to repository artifacts.

### **2.1 Dataset Acquisition – Completed**

We obtained three datasets:

* **Traffic Volume (Chicago Open Data Portal)**
  Stored: `traffic.csv`, `traffic2.csv`
* **Weather Data (Open-Meteo API)**
  Stored: `Weather.csv`
* **Air Quality (Chicago Open Data Portal)**
  Stored: `Air.csv`, `AirQuality.csv`

Acquisition details are documented in `Project.ipynb` under
**“Data Sources + Acquisition Details + Ethical Handling.”**

### **2.2 Storage and Organization – Completed**

* Selected tabular storage using CSV files.
* Organized datasets in repository root for transparency.
* Final merged dataset: `final_dataset.csv`
* Documented in `ProjectPlan.md` and `Project.ipynb`.

### **2.3 Data Cleaning – Completed (Documentation Pending)**

Completed cleaning tasks:

* Date parsing and standardization
* Column renaming for consistency
* Handling missing values
* Standardizing location fields
* Removing duplicates

Cleaning steps implemented in `Project.ipynb`.

### **2.4 Data Integration – Completed**

We merged all datasets using:

* **date**
* **location**

Result stored in `final_dataset.csv`.

### **2.5 Ethical Data Handling – Completed**

* All datasets come from public open-data portals with no personal information.
* Complied with usage terms for Chicago Open Data and Open-Meteo.
* Documented in `Project.ipynb`.

### **2.6 Workflow Automation – Not Started**

Planned: Snakemake workflow integrating all steps from acquisition → cleaning → merging → analysis.

### **2.7 Data Quality Assessment – Not Started**

Initial cleaning is done, but a formal *quality assessment report* is still needed.

### **2.8 Metadata and Documentation – Not Started**

Data dictionary and metadata schema will be added for final submission.

---

## **3. Updated Timeline**

| Task                                | Status          | Expected Completion |
| ----------------------------------- | --------------- | ------------------- |
| Dataset acquisition                 | **Done**        | Completed           |
| Cleaning and enrichment             | **Done**        | Completed           |
| Data integration                    | **Done**        | Completed           |
| Ethical data handling documentation | **Done**        | Completed           |
| Data quality assessment             | **Not started** | Nov 25              |
| Data cleaning documentation         | **In progress** | Nov 25              |
| Workflow automation (Snakemake)     | **Not started** | Dec 1               |
| Data dictionary + metadata          | **Not started** | Dec 3               |
| Analysis + visualizations           | **Not started** | Dec 5               |
| README final report                 | **Not started** | Dec 8               |
| Final GitHub Release                | **Not started** | Dec 10              |

Overall, the project remains on track for the Milestone 4 deadline.

---

## **4. Changes to the Project Plan**

We made several small adjustments based on TA feedback and our progress:

### **4.1 Replacing Placeholder Names**

ProjectPlan.md originally contained placeholders such as [Your Name #1] and [Your Name #2]. These have now been replaced with our real names.

### **4.2 Added Dataset URLs**

We updated the Project Plan to include the full direct URLs to:

* Chicago Traffic dataset
* Chicago Air Quality dataset
* Open-Meteo Weather API

### **4.3 Better Defined Integration Strategy**

We decided to merge using **date** + **location**, as this produced the cleanest join across datasets.

### **4.4 Additional Weather Dataset Removed**

Originally, we considered a third weather dataset, but after testing we determined it was unnecessary and kept the Open-Meteo dataset only.

No structural changes have been made to the main objectives of the project.

---

## **5. Next Steps**

We have completed the full data preparation phase. The following tasks remain for final submission:

### **5.1 Data Quality Assessment (Module 9)**

* Perform profiling on each dataset.
* Document missing values, inconsistencies, and limitations.

### **5.2 Data Cleaning Documentation (Module 10)**

* Summarize all cleaning operations performed in the notebook.
* Export a reproducible cleaning script.

### **5.3 Workflow Automation (Modules 11–12)**

* Build a Snakemake workflow automating:

  * Loading
  * Cleaning
  * Merging
  * Analysis + visualizations

### **5.4 Reproducibility Package (Module 13)**

* Create `requirements.txt`
* Add instructions for re-running the workflow
* Provide dataset acquisition instructions

### **5.5 Metadata & Data Dictionary (Module 15)**

* Provide variable definitions, units, and schema.

### **5.6 Analysis & Visualizations**

* Create figures for traffic–weather–air interactions.
* Add analysis results to final README.

### **5.7 Box Folder Setup**

* Upload final dataset to Box
* Add shareable link in README
* Add to `.gitignore`

### **5.8 Final Report (README.md)**

* Write full project narrative
* Add citations, reproduction steps, findings, and metadata
* Prepare final release (`final-project`)

These steps will complete all remaining project requirements.

---

## **6. Individual Contributions**

### **Rishabh Shahh**

* Created StatusReport.md and updated ProjectPlan.md.
* Added acquisition + ethical handling documentation to Project.ipynb.

### **Atharva Awasthi**

* Collected and cleaned traffic, weather, and air datasets.
* Performed initial integration and generated `final_dataset.csv`.
