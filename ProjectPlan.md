# **Project Plan – Milestone 2**

## **Project Title**

**Smart City Data Pipeline: Connecting Traffic, Weather, and Air Quality Data**

## **Team Members**

* **Rishabh Shahh** – Data acquisition, cleaning, integration, documentation
* **Atharva Awasthi** – Workflow structure, analysis development, automation

---

## **1. Overview**

The goal of this project is to build a simple, end-to-end data pipeline that connects three types of open data from the City of Chicago: **traffic volume**, **weather conditions**, and **air quality measurements**. By combining these datasets, we want to explore how daily traffic patterns and weather relate to local air quality.

This project follows the full data lifecycle—from collecting datasets, storing and organizing them, cleaning and integrating them, and finally producing a reproducible workflow and analysis. The final product will be an automated, transparent pipeline with complete documentation.

---

## **2. Research Questions**

Our project is guided by the following questions:

1. **How do traffic levels relate to daily air quality in Chicago?**
2. **Do weather conditions (temperature, humidity, wind) appear to influence air quality patterns?**
3. **Are there observable trends where traffic + weather together predict higher or lower pollution levels?**

These questions can be answered using descriptive analysis and simple exploratory visualizations.

---

## **3. Datasets**

We will use **three independent datasets**, each coming from a trustworthy open-data source. All datasets include **date** and **location**, which allow them to be merged into a single table.

### **Dataset 1 — Traffic Volume (Chicago Open Data)**

* **URL:** [https://data.cityofchicago.org/Transportation/Traffic-Tracker-Historical-Congestion-Estimates-by/t2qc-9pjd](https://data.cityofchicago.org/Transportation/Traffic-Tracker-Historical-Congestion-Estimates-by/t2qc-9pjd)
* **Format:** CSV
* **Key Columns:** `date`, `street`, `congestion_level`
* **Purpose:** Measures congestion and traffic conditions across Chicago.

### **Dataset 2 — Air Quality (Chicago Open Data)**

* **URL:** [https://data.cityofchicago.org/Environment/Air-Quality-Monitoring/hgnt-xx2f](https://data.cityofchicago.org/Environment/Air-Quality-Monitoring/hgnt-xx2f)
* **Format:** CSV
* **Key Columns:** `date`, `monitor_name`, `pm25`, `ozone`
* **Purpose:** Provides pollutant readings from Chicago monitoring stations.

### **Dataset 3 — Weather Data (Open-Meteo API)**

* **API:** [https://api.open-meteo.com/v1/](https://api.open-meteo.com/v1/)
* **Format:** JSON → converted to CSV
* **Key Columns:** `date`, `temperature`, `wind_speed`, `humidity`
* **Purpose:** Provides daily weather measurements for the Chicago area.

All three datasets are stored in the project repository as:

* `traffic.csv`
* `AirQuality.csv`
* `Weather.csv`

---

## **4. Roles and Responsibilities**

### **Rishabh Shahh**

* Acquire datasets and verify licensing/ethical use
* Clean and standardize datasets
* Perform initial integration into a single dataset
* Maintain documentation in Project.ipynb

### **Atharva Awasthi**

* Develop workflow automation (Snakemake or script-based)
* Create analysis and visualizations
* Contribute to metadata, data dictionary, and README
* Assist with integration and final presentation

Both team members will contribute commits regularly to ensure clear evidence of participation.

---

## **5. Timeline**

| Task                                     | Owner             | Deadline | Status      |
| ---------------------------------------- | ----------------- | -------- | ----------- |
| Dataset acquisition                      | Rishabh           | Oct 10   | Done        |
| Initial cleaning + standardization       | Rishabh           | Oct 15   | Done        |
| Dataset integration                      | Rishabh + Atharva | Oct 20   | Done        |
| Ethical review + licensing documentation | Rishabh           | Oct 22   | Done        |
| Workflow structure setup                 | Atharva           | Nov 20   | In progress |
| Data quality assessment                  | Both              | Nov 25   | Upcoming    |
| Analysis + visualizations                | Atharva           | Dec 5    | Upcoming    |
| Final metadata + data dictionary         | Both              | Dec 5    | Upcoming    |
| Final README + reproducibility           | Both              | Dec 8    | Upcoming    |
| Final release                            | Both              | Dec 10   | Upcoming    |

We are currently ahead of schedule for data preparation.

---

## **6. Ethical, Legal, and Policy Considerations**

All data comes from open sources with **public licenses** allowing reuse:

* Chicago Open Data Portal: data is free to use under the City’s Open Data Terms.
* Open-Meteo API: unrestricted use for academic and research purposes.

There is **no personal or identifying data** in any dataset.
All sources are properly cited in the final report, and no terms of service are violated.

We will also:

* Document dataset licenses in the README
* Store all raw data without modification
* Provide clear attribution to data providers

---

## **7. Storage and Organization Strategy**

We chose a simple, transparent folder structure:

```
/project
    /raw_data
        traffic.csv
        AirQuality.csv
        Weather.csv
    /processed
        final_dataset.csv
    /scripts
        integrate.py
        clean.py
    ProjectPlan.md
    StatusReport.md
    Project.ipynb
```

* Raw data stays untouched.
* Processed data is generated by scripts or workflow rules.
* Notebook provides visible documentation of decisions.

---

## **8. Extraction & Enrichment**

We will:

* Parse dates and convert everything to `YYYY-MM-DD`
* Standardize location fields so joins work cleanly
* Add derived variables such as:

  * “AQI_Category”
  * “Traffic_Intensity_Score”
  * “Feels_Like_Temperature”

This step is partly complete; we will finalize enrichment after formal data quality checks.

---

## **9. Data Integration Strategy**

Datasets will be merged using:

* **Primary Key 1:** `date`
* **Primary Key 2:** `location` (or nearest comparable field)

We already produced a merged dataset (`final_dataset.csv`) through cleaning + joining in Python.

---

## **10. Constraints**

* Some weather variables may have missing values.
* Chicago traffic coverage varies by neighborhood.
* API rate limits require caching weather data if re-pulling.

These constraints will be included in the data quality summary.

---

## **11. Gaps / Unknowns**

* Final visualization strategy is still being decided.
* We may include simple correlation metrics if data allows.
* Workflow automation is still to be implemented using Snakemake.

---

## **12. Expected Final Deliverables**

By the end of the project, we will provide:

* Full analysis notebook
* Snakemake workflow + run-all script
* Cleaned + merged dataset (`final_dataset.csv`)
* Data dictionary + metadata (DataCite style)
* README with reproducibility instructions
* Box folder with processed data
* All raw datasets + citations

---

**This plan has been updated according to TA feedback and reflects the true structure and progress of our project.**
