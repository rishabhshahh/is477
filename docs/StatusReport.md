# **Status Report – Milestone 3**

## **Project Title**

**Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data**

## **Team Members**

* **Rishabh Shah**
* **Atharva Awasthi**

---

## **1. Overview of Progress**

Since submitting our Project Plan, we have made strong progress on the core parts of our project. We successfully collected, cleaned, and merged three datasets (Traffic, Weather, and Air Quality), all focused on the City of Chicago. Our goal is to study how traffic levels and weather conditions relate to daily air quality.

We now have a fully combined dataset (`final_dataset.csv`) that integrates all sources using the shared fields **date** and **location**. We also began building our Python scripts and workflow structure for automation and reproducibility.

Overall, the project is on schedule, and we have completed the entire data preparation stage.

---

## **2. Updates on Tasks from the Project Plan**

### **Data Collection**

* We collected the following datasets and added them to the repository:

  * `traffic.csv` and `traffic2.csv`
  * `Weather.csv`
  * `Air.csv` and `AirQuality.csv`
* These files are stored in the root folder of the repository.

### **Data Cleaning**

* Cleaned each dataset by:

  * Standardizing dates to the format `YYYY-MM-DD`
  * Filtering to Chicago-based locations
  * Removing duplicate or invalid rows
  * Renaming inconsistent columns

### **Data Integration**

* Successfully merged all datasets into **one integrated file**:
  **`final_dataset.csv`**
* Joined on:

  * `date`
  * `location`
* This file is in the repository and is ready for analysis.

### **Scripts and Workflow**

* We started building the workflow for automation:

  * A Jupyter Notebook (`Project.ipynb`) that contains early analysis and testing
  * Scripts for cleaning and merging will be added before final submission
* We will convert the workflow into a Snakemake pipeline later in the project.

---

## **3. Updated Timeline**

| Task                           | Status      | Owner   | Target Completion |
| ------------------------------ | ----------- | ------- | ----------------- |
| Collect datasets               | **Done**    | Rishabh | Oct 25            |
| Clean datasets                 | **Done**    | Rishabh | Nov 1             |
| Integrate datasets             | **Done**    | Rishabh | Nov 2             |
| Build scripts + automation     | In Progress | Atharva | Nov 20            |
| Exploratory analysis + graphs  | In Progress | Atharva | Nov 30            |
| Final report + reproducibility | Not Started | Both    | Dec 10            |

We are currently on track according to this timeline.

---

## **4. Changes Made to the Original Project Plan**

* We originally considered analyzing multiple cities, but we decided to **focus only on Chicago** to make the datasets align more easily.
* We added a **third dataset (Air Quality)** to support deeper analysis.
* We adjusted the workflow to begin with Python notebooks before moving fully into automation tools like Snakemake.
* We improved our merging strategy by using `date` and `location` as our primary integration keys.

---

## **5. Challenges Encountered**

* Some datasets had missing or inconsistent dates that required fixing.
* Weather data from our API needed unit normalization and formatting adjustments.
* Air quality data required cleanup due to multiple file versions (`Air.csv`, `AirQuality.csv`).
* Aligning the datasets to the same frequency (daily) required aggregation steps.

Despite these challenges, all issues were resolved, and the integrated dataset is complete.

---

## **6. Next Steps**

* Build the full automated workflow using Python and Snakemake.
* Create visualizations showing relationships between:

  * Traffic congestion and PM2.5
  * Weather (temperature, humidity, wind) and AQI
* Begin writing the final project report (`README.md`).
* Upload output data to Box and prepare reproducibility documentation.

---

## **7. Individual Contributions**

### **Rishabh Shah**

* Collected all datasets (traffic, weather, air quality)
* Cleaned and formatted all raw data files
* Created the final integrated dataset (`final_dataset.csv`)
* Updated data documentation and verified dataset accuracy

### **Atharva Awasthi**

* Organized the repository structure
* Started building automation scripts
* Created initial exploratory notebook
* Worked on preparing documentation for workflow and metadata

---

## **8. Repository Artifacts (So Far)**

* `traffic.csv`
* `traffic2.csv`
* `Weather.csv`
* `Air.csv`
* `AirQuality.csv`
* `final_dataset.csv`
* `Project.ipynb`
* `ProjectPlan.md`
* `StatusReport.md`

---

## **9. Summary**

Overall, we have completed the foundation of our project: collecting, cleaning, and integrating all necessary datasets. The data is now ready for analysis and automation. We are on schedule and moving into the workflow and visualization phase.
