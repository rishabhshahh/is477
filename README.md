# Smart City Data Pipeline: Integrating Traffic, Weather, and Air Quality in Chicago

## Contributors

* **Rishabh Shah**
* **Atharva Awasthi**

## Summary

This project presents a fully reproducible smart city data pipeline that integrates traffic congestion, weather conditions, and air quality measurements for the City of Chicago. The primary motivation for this project is the growing importance of data-driven decision-making in urban environments, especially in areas related to transportation planning, environmental policy, and public health. As cities continue to grow and vehicle usage increases, understanding the relationship between traffic behavior, meteorological conditions, and air pollution becomes increasingly critical.

The central research question guiding this project is:  
**How do traffic congestion and weather conditions relate to air quality levels in Chicago?**  
More specifically, we aim to explore whether higher congestion tends to coincide with increased pollution levels, and how environmental factors such as wind speed, temperature, and precipitation influence the concentration and dispersion of airborne pollutants.

Rather than focusing on predictive modeling, the primary emphasis of this project is on the **data lifecycle, automation, reproducibility, and transparency** of an end-to-end data workflow. The technical goal is to demonstrate how multiple independent datasets from different sources can be collected, cleaned, integrated, verified, and reproduced using modern data engineering practices. This approach aligns closely with the core learning objectives of IS477, which emphasize the importance of responsible data handling, documentation, and workflow provenance.

Three independent datasets are used in this project: a Chicago traffic congestion dataset, a Chicago air pollution dataset, and a Chicago weather dataset. Each dataset originates from a different public source and contains different data structures, schemas, and update mechanisms. The challenge of this project lies in harmonizing these heterogeneous sources into a single unified dataset that supports meaningful analysis. This requires careful attention to timestamp alignment, location matching, unit standardization, and quality validation.

The project follows the complete **data lifecycle**, beginning with raw data acquisition and ending with a fully reproducible analysis pipeline. The major stages of the lifecycle implemented in this project include data collection, storage and organization, data quality assessment, data cleaning and enrichment, data integration, automation, provenance tracking, and reproducibility validation. All processing steps are implemented using Python, leveraging the pandas and NumPy libraries for data transformation, and Snakemake for workflow automation.

An important component of this project is the use of **SHA-256 cryptographic hashing** to ensure dataset integrity and support reproducibility. Cryptographic hashes are generated automatically for both the processed dataset and the cleaned dataset. These hashes allow anyone reproducing the project to verify that their datasets exactly match the original outputs used in the analysis. If any change occurs to the data—whether through corruption, modification, or version mismatch—the SHA-256 values will immediately differ, signaling a reproducibility issue. This approach provides strong guarantees of data transparency and trustworthiness.

Workflow automation is implemented using **Snakemake**, which orchestrates all steps of the pipeline using a Directed Acyclic Graph (DAG). The automated workflow includes rules for hashing the processed dataset, cleaning the dataset, hashing the cleaned output, and validating the completion of the entire pipeline. This ensures that the workflow can be executed from start to finish using a single command and that all transformations occur in the correct order with full provenance tracking.

The final outputs of the project include a merged processed dataset and a fully cleaned analytical dataset. The processed dataset contains aligned traffic, weather, and air quality values, while the cleaned dataset applies additional filtering, validation, and feature enrichment. The cleaned dataset includes derived temporal features such as year, month, day of week, and hour, which support time-based analysis. These outputs serve as the foundation for interpreting relationships between urban mobility, meteorological conditions, and pollution dynamics.

In addition to its technical contributions, this project also emphasizes **ethical data handling**. All datasets used are publicly available and contain no personally identifiable information. No scraping of protected systems occurred, and all usage complies with the terms and conditions of the original data providers. As a result, the project avoids privacy risks, consent violations, and legal concerns.

Ultimately, this project demonstrates how a transparent and reproducible data pipeline can be constructed to support smart city research. It shows how data alone is not enough—what matters equally is how the data is collected, validated, transformed, verified, and documented. By emphasizing automation, version control, cryptographic verification, and structured documentation, this project provides a solid foundation for future analytical work, policy analysis, and urban data science research.

## Project Outputs

* **Processed Dataset:**
  `data/processed/final_dataset.csv`

* **Cleaned Dataset:**
  `data/cleaned/final_dataset_cleaned.csv`

* **SHA-256 Hash Values:**

```
Processed SHA-256: fbf7fe8577cbd3b11763907cb945b6bdc634908b783e3a265a6376435f82436f
Cleaned SHA-256:   e4bb83c997a68fc7f08767f7060df434b18500ff1d9d642faa92c718fd007d21
```

* **Automated Workflow:**
  Executed using **Snakemake** with full provenance tracking.

## Data Profile

This project integrates three independent public datasets related to traffic congestion, weather conditions, and air pollution in the City of Chicago. These datasets originate from different platforms, use different schemas, and vary in update frequency and structure, making them well suited for a real-world data integration and reproducibility case study. All datasets are publicly accessible, contain no personally identifiable information, and are used in accordance with their published terms of use.

---

### 1. Chicago Air Pollution Dataset (Kaggle)

**Source:**  
https://www.kaggle.com/datasets/asjad99/chicago-air-pollution  

This dataset provides historical air pollution measurements for Chicago and serves as the primary environmental health indicator in this project. It includes pollutant concentration values such as:

- PM2.5 (fine particulate matter)
- PM10 (coarse particulate matter)
- Nitrogen Dioxide (NO₂)
- Sulfur Dioxide (SO₂)
- Carbon Monoxide (CO)
- Air Quality Index (AQI)

These pollutants are widely used in environmental and public health research because they directly affect respiratory and cardiovascular health. The dataset includes time-based measurements that allow it to be aligned with traffic and weather data.

**Format and Access:**  
The dataset is distributed as a CSV file through Kaggle, making it easy to download and process using standard data science tools such as pandas. Since Kaggle hosts user-contributed datasets, the responsibility of validating data quality and completeness falls on the user, which makes this dataset particularly appropriate for reproducibility and quality assessment exercises.

**Ethical and Legal Considerations:**  
This dataset contains **no personal data, no tracking information, and no identifiable individuals**. All values represent aggregate environmental sensor readings. The dataset is shared publicly through Kaggle and is intended for educational and research use. No consent or privacy issues are involved. The project adheres strictly to Kaggle’s dataset usage policies.

---

### 2. Chicago Traffic Congestion Dataset (Data.gov / Chicago Open Data)

**Source:**  
https://catalog.data.gov/dataset/chicago-traffic-tracker-historical-congestion-estimates-by-segment-2024-current  

This dataset contains traffic congestion measurements collected by the City of Chicago’s Traffic Tracker system. It provides information on roadway traffic performance across multiple street segments, including:

- Traffic speed
- Street and directional attributes
- Segment identifiers
- Congestion levels
- Bus volume and message counts
- Latitude and longitude of road segments

This dataset plays a crucial role in the project by representing **urban mobility patterns**, which are directly related to vehicular emissions and air quality.

**Format and Access:**  
The dataset is accessible through Data.gov and the City of Chicago Open Data portal. It is distributed in CSV format and updated regularly. Data.gov datasets are provided under permissive public data licenses, allowing free educational and research use. We downloaded snapshots of the dataset and stored them as `traffic.csv` and `traffic2.csv` in the repository.

**Ethical and Legal Considerations:**  
This dataset contains **no personal driver data**, license plate numbers, or individual tracking. It represents **aggregated roadway-level traffic measurements**, fully compliant with public open data standards. No consent requirements apply because the data does not identify individuals.

---

### 3. Chicago Weather Dataset (Kaggle / Open-Meteo Derived)

**Source:**  
https://www.kaggle.com/code/sheemazain/weather-dataset-2024/notebook  

This weather dataset provides meteorological conditions for Chicago and is derived from the Open-Meteo API. It includes atmospheric variables such as:

- Temperature
- Precipitation
- Humidity
- Wind Speed
- Atmospheric Pressure

Weather conditions have a well-documented effect on both traffic behavior and air pollutant dispersion. For example, precipitation may reduce traffic volume, while wind speed may influence how pollutants accumulate or dissipate.

**Format and Access:**  
This dataset is provided as a CSV file with daily and hourly time stamps, downloaded from Kaggle where it is shared in notebook format. Because this dataset is derived from Open-Meteo, it adheres to Open-Meteo’s permissive usage terms for research and education.

**Ethical and Legal Considerations:**  
This dataset contains only **non-sensitive atmospheric sensor readings**. There is no human subject data, no tracking, and no personal identifiers. All data is legally redistributable for educational purposes.

---

## Data Integration Alignment

These three datasets are integrated based on two shared core attributes:

- **Time (date and hour where available)**
- **Location (Chicago street or region mapping)**

Each dataset originally used different column naming conventions and time formats. These were standardized during processing to allow consistent merging. The integration resulted in a single unified file:

data/processed/final_dataset.csv

After cleaning and enrichment, the final analytical dataset is:

data/cleaned/final_dataset_cleaned.csv


---

## Data Volume and Storage

All datasets are stored locally in CSV format due to their manageable size. The project does not require database storage due to relatively modest file sizes and the focus on reproducibility rather than high-throughput querying.

Processed and cleaned outputs are version-controlled through GitHub, while cryptographic SHA-256 hashes are used to verify data integrity across pipeline executions.

---

## Summary of Ethical and Legal Compliance

All datasets used in this project satisfy the following conditions:

- ✅ Publicly available  
- ✅ No personally identifiable information  
- ✅ No consent requirements  
- ✅ Permitted for educational and research use  
- ✅ Fully documented source links  
- ✅ No scraping of restricted content  

As a result, this project fully complies with ethical data use standards and avoids privacy, licensing, or regulatory violations.

---

## Data Limitations

Although the datasets are reliable for educational use, some limitations remain:

- Data coverage is not continuous across all locations and times.
- Some records contain missing or inconsistent values.
- Sensor-based measurements may include observational noise.
- Kaggle datasets may contain unknown preprocessing steps by the original contributors.

These limitations are addressed through formal data quality checks and cleaning procedures detailed in the next section.

## Ethical, Legal, and Policy Compliance

All datasets used in this project meet ethical and legal compliance standards:

* All datasets are publicly available
* No personally identifiable information (PII) is included
* No medical, biometric, or private user data is used
* No restricted scraping or unauthorized access occurred
* Usage complies with Chicago Open Data and Kaggle terms

As a result:

* **No consent violations exist**
* **No privacy risks exist**
* **Full research transparency is maintained**

## Dataset Integration Overview

All datasets were integrated using **temporal and spatial alignment** across:

* `TIME`
* `DATE`
* `SEGMENT_ID / LOCATION`

This creates a unified analytical dataset that allows direct comparison between:

* Traffic activity
* Weather conditions
* Air pollution levels

The integration output is stored in:

* `data/processed/final_dataset.csv`
* `data/cleaned/final_dataset_cleaned.csv`

## Data Quality

A formal data quality assessment was conducted to evaluate the reliability, consistency, and usability of each dataset before and after integration. Because this project integrates three independent public data sources (traffic, air pollution, and weather), careful attention to data quality was required to ensure meaningful results and full reproducibility. All quality checks and cleaning operations were implemented using Python with pandas and NumPy, primarily through the script `scripts/clean_data.py`.

---

## 1. Initial Data Quality Issues Observed

Each dataset exhibited common real-world data quality challenges. These issues were systematically identified before cleaning and integration:

### 1.1 Missing Values  
Missing values appeared across multiple variables, especially in:

- Traffic speed (`SPEED`)
- Weather variables such as precipitation (`PRCP`) and humidity (`HMDT`)
- Air pollution variables such as PM2.5, PM10, and gaseous pollutants

Missing values occurred due to:
- Sensor downtime
- Partial reporting on certain days
- Gaps in time-series coverage

### 1.2 Inconsistent Time Formats  
The `TIME` column appeared in different formats across datasets:
- String timestamps
- Date-only records
- Mixed date-time encodings

This inconsistency initially prevented reliable merges.

### 1.3 Inconsistent Text Fields  
Street names and directional fields contained:
- Extra whitespace
- Mixed capitalization
- Inconsistent formatting across datasets

Examples included:
- `"north"` vs `"North"`
- `"  Main St  "` with excess spaces

### 1.4 Numeric Type Errors  
Several numeric fields were imported as strings due to:
- Improper CSV formatting
- Embedded non-numeric characters

This affected columns such as:
- Traffic speed
- Segment length
- Pollutant concentration values

### 1.5 Duplicated Records  
Duplicate rows were present in the traffic dataset due to:
- Repeated reports at identical timestamps
- System-level message duplication

Duplicates distorted congestion counts and required removal.

---

## 2. Data Quality Controls Implemented

All quality improvements were implemented systematically using a custom Python function inside `clean_data.py`. This ensured both transparency and reproducibility.

### 2.1 Time Standardization

The `TIME` column was converted into a standardized pandas datetime format:

```python
df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce")
````

Invalid timestamps were automatically converted to missing values. Additional time features were extracted:

* `DATE`
* `YEAR`
* `MONTH`
* `DAY_OF_WEEK`
* `HOUR`

These derived fields support temporal aggregations and improve interpretability.

---

### 2.2 Text Field Normalization

Text columns such as street names and location descriptors were cleaned by:

* Trimming whitespace
* Collapsing multiple spaces
* Standardizing capitalization

```python
df[c] = df[c].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
df[c] = df[c].str.upper()
```

This reduced inconsistencies during location-based integration.

---

### 2.3 Numeric Type Enforcement

All quantitative fields were explicitly converted to numeric types using:

```python
df[c] = pd.to_numeric(df[c], errors="coerce")
```

This forced invalid numeric values to become missing and prevented incorrect arithmetic calculations.

---

### 2.4 Outlier and Range Validation

Logical value ranges were enforced for key quantitative variables:

* `SPEED` greater than 120 mph marked as invalid
* `LENGTH` values less than or equal to zero removed
* Negative pollution concentrations removed
* Negative precipitation removed
* Negative humidity, wind speed, and pressure invalidated

These rules removed physically impossible or unreliable sensor readings.

---

### 2.5 Duplicate Record Removal

Duplicates were removed using timestamp and segment identifiers:

```python
df = df.drop_duplicates(subset=["TIME", "SEGMENT_ID"], keep="first")
```

This ensured that each traffic segment was represented only once per timestamp.

---

## 3. Integration-Level Quality Checks

After individual dataset cleaning, the merged dataset was assessed for:

* Join completeness
* Unexpected record duplication post-merge
* Time misalignment artifacts
* Location mismatches

Records failing integration consistency checks were retained but flagged through missing merged values, preserving transparency while maintaining dataset integrity.

---

## 4. Post-Cleaning Quality Improvements

After applying all quality controls, the following improvements were observed:

* ✅ All timestamps standardized into a single format
* ✅ All numeric fields safely cast into numeric dtype
* ✅ All text fields normalized for clean integration
* ✅ Unrealistic physical values removed
* ✅ Duplicate traffic records eliminated
* ✅ Temporal features added for downstream analysis

The final cleaned dataset is saved as:

```
data/cleaned/final_dataset_cleaned.csv
```

---

## 5. Cryptographic Integrity Verification

To ensure full transparency and reproducibility, SHA-256 hashes were generated for:

* The **processed merged dataset**
* The **final cleaned dataset**

These hashes were generated automatically using Snakemake rules:

```
results/processed_sha256.txt
results/cleaned_sha256.txt
```

Example recorded hashes:

* Processed SHA-256:
  `fbf7fe8577cbd3b11763907cb945b6bdc634908b783e3a265a6376435f82436f`

* Cleaned SHA-256:
  `e4bb83c997a68fc7f08767f7060df434b18500ff1d9d642faa92c718fd007d21`

These values allow independent verification that the datasets remain unchanged across executions.

---

## 6. Remaining Data Quality Limitations

Despite extensive cleaning, some unavoidable limitations remain:

* Some time periods lack full sensor coverage
* Pollution levels may fluctuate due to short-term events not reflected in traffic
* Weather sensors reflect regional rather than street-level conditions
* Kaggle-based datasets may contain undocumented preprocessing steps

These limitations were preserved rather than artificially corrected to maintain scientific transparency.

---

## 7. Overall Data Quality Assessment

After completing all quality checks and cleaning operations, the final dataset meets the following criteria:

* ✅ Consistent time formatting
* ✅ Clean numeric measurements
* ✅ Validated physical ranges
* ✅ Clean textual location fields
* ✅ Verified dataset integrity via SHA-256
* ✅ Fully reproducible cleaning process

As a result, the dataset is assessed as **high-quality and suitable for reproducible smart city analysis** within the scope of this project.

## Data Cleaning

Data cleaning was conducted using **Python (`pandas`, `numpy`)** and implemented in:

* `scripts/clean_data.py`
* `notebooks/Project.ipynb`

### Cleaning Function Overview

All transformations are performed through this function:

```python
def clean_final_df(df):
```

### Cleaning Steps Applied

### 1. Time Standardization

```python
df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce")
```

Ensures consistent timestamps across all datasets.

### 2. Text Normalization

Standardized values for:

* `STREET`
* `DIRECTION`
* `FROM_STREET`
* `TO_STREET`
* `STREET_HEADING`
* `COMMENTS`
* `START_LOCATION`
* `END_LOCATION`

Operations:

* Trim whitespace
* Collapse multiple spaces
* Enforce uppercase where required

### 3. Numeric Casting

All numeric variables are type-cast using:

```python
pd.to_numeric(..., errors="coerce")
```

Includes:

* Traffic values (speed, counts)
* Weather variables
* Air pollution values

### 4. Outlier Handling

| Variable   | Constraint Applied |
| ---------- | ------------------ |
| Speed      | 0 ≤ Speed ≤ 120    |
| Length     | Length > 0         |
| Bus Count  | ≥ 0                |
| AQI        | ≥ 0                |
| Pollutants | ≥ 0                |

Out-of-range values were set to `NaN`.

### 5. Duplicate Removal

Duplicates removed using:

```python
df.drop_duplicates(subset=["TIME", "SEGMENT_ID"])
```

### 6. Feature Engineering

Derived variables added:

* `DATE`
* `YEAR`
* `MONTH`
* `DAY_OF_WEEK`
* `HOUR`

### Output

Final cleaned dataset generated as:

```
data/cleaned/final_dataset_cleaned.csv
```

## Workflow Automation & Provenance (Snakemake)

This project uses a **Snakemake workflow** to fully automate all transformation steps.

### Automated Rules

| Rule             | Input                                    | Output                                   |
| ---------------- | ---------------------------------------- | ---------------------------------------- |
| `hash_processed` | `data/processed/final_dataset.csv`       | `results/processed_sha256.txt`           |
| `clean_data`     | `data/processed/final_dataset.csv`       | `data/cleaned/final_dataset_cleaned.csv` |
| `hash_cleaned`   | `data/cleaned/final_dataset_cleaned.csv` | `results/cleaned_sha256.txt`             |
| `all`            | All dependencies                         | Full pipeline                            |

### Successful DAG Execution

From your full run:

```
Job stats:
job               count
all                   1
clean_data            1
hash_cleaned          1
hash_processed        1
```

✔ All workflow steps executed successfully
✔ Logs captured in `.snakemake/log/`
✔ Re-execution confirms full reproducibility

## Reproducibility via SHA-256 Integrity Checks

To ensure **cryptographic reproducibility**, SHA-256 hashes were generated automatically.

### Processed Dataset

```
fbf7fe8577cbd3b11763907cb945b6bdc634908b783e3a265a6376435f82436f
```

### Cleaned Dataset

```
e4bb83c997a68fc7f08767f7060df434b18500ff1d9d642faa92c718fd007d21
```

These hashes allow graders and researchers to:

* Verify dataset authenticity
* Detect corruption
* Confirm identical reproduction across systems

## Provenance Tracking

Provenance is fully captured through:

* ✔ Snakemake execution DAG
* ✔ SHA-256 hash records
* ✔ Script-based transformations
* ✔ GitHub commit versioning

Complete traceability exists from:

```
Raw Data → Processed → Cleaned → Hashed → Analyzed
```

Findings:
When I finished cleaning and integrating the traffic, weather and air quality datasets the first thing I noticed was that the relationships between traffic behavior and weather were not as strong as I expected them to be and this became clear pretty early in the analysis when I started looking at basic correlations and grouped averages. Normally you would assume that colder temperatures or heavy rain would slow vehicles down noticeably, but when I visualized average speed across temperature bins the numbers barely moved at all and they stayed clustered in the same range regardless of whether it was freezing or warm. The precipitation results were similar because even though I grouped rainfall into ranges from no rain up to heavier amounts, the average speeds only dropped by maybe one mile per hour at most, which is not enough to say that precipitation meaningfully disrupts city traffic in this dataset. The heatmap reinforced this idea because speed had correlations extremely close to zero with temperature, precipitation and wind speed. This is one of the clearest signals in the findings, that weather has limited influence on traffic speed as measured by this dataset and at least over the timespan we observed.
Then I looked at the relationship between air quality and traffic, which I expected to be much stronger because traffic emissions are a known contributor to pollutants like NO2 and sometimes particulate matter. The hourly plot made sense since during classic rush hour periods like early morning and late afternoon NO2 levels went up and traffic speed dipped slightly, which kind of aligns with general intuition. But the interesting part came when comparing NO2 to the congestion index at the individual segment level, because almost all the points were clustered near a congestion index close to zero. NO2 remained high even in segments that showed practically no congestion, so there was no visible upward trend or relationship there. This suggests that local congestion within single short segments is not what explains NO2 levels, rather NO2 reflects overall citywide emissions combined with weather and atmospheric conditions that trap pollutants or disperse them. This is important because it means the dataset does not capture enough local variation in congestion to explain pollutant spikes and it also means that NO2 behaves on a larger spatial scale than traffic speeds on a single road segment.
The most interesting patterns came when I compared weather variables with air quality. Wind speed had a very clear association with PM2.5 because as wind increased the PM2.5 levels consistently decreased, and that makes sense physically because wind disperses fine particles more easily. PM10 behaved a little differently since it went up during breezy conditions, probably because larger particles get kicked up from the ground, and then dropped again at higher winds. Rainfall did not show much of a relationship with particulate levels which was surprising but could be due to the type of rainfall events in the dataset, maybe they were not strong enough to wash out pollutants. Humidity and atmospheric pressure did not show strong relationships either, although there were hints that high humidity might correlate with slightly higher particulate concentrations, which might relate to how particles absorb moisture.
Finally when combining all findings together the overall picture is that traffic speed in this dataset is mostly unaffected by weather, air quality is influenced more by large scale traffic flows and atmospheric mixing, and weather especially wind plays a noticeable role in how pollutants spread or accumulate. These findings highlight the complexity of urban environmental systems and show that single variable explanations often fall short.

Reproducing
To reproduce this project the first thing someone needs to do is set up the correct software environment. They should install Python 3 along with the required libraries including pandas, numpy, seaborn and matplotlib, and they also need Snakemake since the entire workflow depends on it to run in a consistent and automated way. Git should be installed as well so that the repository can be downloaded without any issues.
The next step is to clone the published GitHub repository for this project. Once the user runs the clone command and opens the folder, they should confirm that the directory structure looks the same as the one described in the documentation. The main folders they need include data, scripts, results, notebooks and the Snakefile which sits in the root of the project. Everything required to run the workflow is already contained within the repository so there is no need to reconfigure anything.
After navigating into the project directory the user can reproduce the cleaning and processing workflow by running Snakemake. This requires only a single command which is simply snakemake followed by the number of cores they want to use. When Snakemake runs it automatically locates the processed dataset in the data folder, generates a SHA 256 hash for it, runs the cleaning script, saves the cleaned dataset into the cleaned folder and then generates a second SHA 256 hash for the cleaned file. When the workflow completes the user should see the cleaned dataset along with two hash files inside the results folder.
At this point the user should verify that the cleaned dataset matches the expected integrity value. The cleaned file will have the SHA 256 fingerprint e4bb83c997a68fc7f08767f7060df434b18500ff1d9d642faa92c718fd007d21 and matching this value confirms that the results were reproduced correctly. If the hash does not match then something about the environment or the dataset inputs is different and the workflow would need to be checked again.
Once the cleaned dataset is reproduced the next step is to open the analysis notebook inside the notebooks folder. The notebook loads the cleaned file and recreates all visualizations and summary statistics used in the findings section. The user should run each cell in order which will regenerate correlation heatmaps, temperature and precipitation comparisons, hourly speed and pollution plots, congestion versus pollution scatterplots and wind category pollution charts. If everything has been reproduced correctly the figures and metrics will look the same as the ones reported in the analysis.
After rerunning the notebook it is a good idea for the user to check their results against the published ones. They should confirm that the number of rows in the cleaned dataset matches the metadata and that all graphs follow the same trends that were described. Summary statistics like averages and correlation values should also line up closely. If anything does not match, they can repeat the workflow to make sure the data was processed the same way.
If the user wants to take reproducibility one step further they can delete the cleaned dataset and hash files, then rerun Snakemake from scratch. If the workflow is truly deterministic, it will generate the exact same cleaned dataset and the exact same SHA 256 hash as before. This is one of the key strengths of using Snakemake along with hashing which together make the project easy to reproduce on any machine.
Finally if the user wants to build the final report, they can render the analysis notebook using Quarto. Running quarto render on the notebook will produce a fresh HTML report that contains all the visualizations and text. At that point the entire project has been fully reproduced starting from the repository all the way to the final results.


## Licenses

### Data Licenses

* ✅ **Chicago Open Data** — Public data under open government license
* ✅ **Kaggle Dataset (Air Pollution)** — Free for academic use
* ✅ **Weather Dataset (Kaggle / API)** — Open research usage

No personally identifiable information (PII) exists in any dataset.

### Software Licenses

All code created for this project is released under:

```
MIT License
```

This allows reuse, modification, and redistribution for academic and research purposes.

## References

### Datasets Used

* Chicago Air Pollution Dataset
  [https://www.kaggle.com/datasets/asjad99/chicago-air-pollution](https://www.kaggle.com/datasets/asjad99/chicago-air-pollution)

* Chicago Traffic Congestion Tracker
  [https://catalog.data.gov/dataset/chicago-traffic-tracker-historical-congestion-estimates-by-segment-2024-current](https://catalog.data.gov/dataset/chicago-traffic-tracker-historical-congestion-estimates-by-segment-2024-current)

* Weather Dataset
  [https://www.kaggle.com/code/sheemazain/weather-dataset-2024/notebook](https://www.kaggle.com/code/sheemazain/weather-dataset-2024/notebook)

  Sivagnanam, Subhashini, Viswanath Nandigam, and Kai Lin. “Introducing the Open Science Chain: Protecting Integrity and Provenance of Research Data.” Practice and Experience in Advanced Research Computing (PEARC ’19), ACM, 2019, pp. 1–5.

### Software Tools Used

* **Python** – Data processing and automation
* **Pandas** – Data wrangling and integration
* **NumPy** – Numeric operations
* **Snakemake** – Workflow automation and provenance
* **Jupyter Notebook** – Analysis and development
* **Git / GitHub** – Version control and collaboration

### Articles & Learning Resources

* Snakemake Documentation – Workflow Automation
  [https://snakemake.readthedocs.io](https://snakemake.readthedocs.io)

* NIST Explanation of SHA-256
  [https://www.nist.gov](https://www.nist.gov)

These resources informed our understanding of **automation, reproducibility, and cryptographic integrity verification**.

Future work:
There are a lot of directions this project could grow in if more time or more detailed datasets were available because while the findings were helpful they also opened up a bunch of new questions about what actually drives congestion and pollution dynamics over time. One of the biggest things that would improve the analysis is having a richer traffic dataset that includes more granular measures of congestion, maybe something like actual vehicle counts or speed variance or lane level occupancy instead of only averaged speeds. The congestion index created from length divided by speed was a decent estimate but it clearly did not capture realistic congestion patterns and because of that it limited how strongly we could interpret the relationship between traffic intensity and pollution spikes. Future work could explore more complex congestion metrics, or even integrate third party traffic APIs that track real time flow or incidents which would give a much fuller picture.
Another major area to expand is the temporal modeling aspect because right now most of the analysis was descriptive, focusing on correlations and group level comparisons, but it would be useful to build predictive models that try to estimate traffic speed or pollution levels based on weather inputs, hour of day, day of week and maybe lagged variables. A multivariate regression or a machine learning model like random forest or gradient boosting could help uncover nonlinear relationships that simple correlations miss. For example weather probably affects pollution indirectly through atmospheric mixing or inversion layers, and those effects might only appear when conditions stack in certain ways. A model could help reveal those interaction effects.
It would also be valuable to expand the spatial dimension of the project. The current dataset has latitude and longitude fields but the analysis did not really use them for spatial clustering or mapping. Future work could look at whether certain regions consistently experience more pollution or slower traffic, maybe near industrial corridors or dense downtown areas. Techniques such as kernel density maps, segment clustering or spatial autocorrelation tests could give a lot more insight into how location matters. You could also merge the dataset with land use data or census socioeconomic data to study environmental justice implications which is becoming a more important area of research.
Another improvement would be refining the air quality integration. The pollutant values likely come from citywide or regional monitoring stations and may not perfectly align with the traffic segment timestamps. If higher resolution sensor networks or mobile air quality monitors were available, the dataset could become a lot more precise and improve the ability to detect localized pollution effects caused by nearby traffic conditions. Future work could also explore additional pollutants like ozone dynamics, which are highly sensitive to temperature and sunlight and might produce much stronger relationships with weather variables.
On the workflow side the Snakemake pipeline could be extended to include full environment reproducibility through something like Conda or containerization with Docker. This would ensure that not only the data processing scripts but also the entire computational environment can be reproduced years from now, which is a growing standard in professional data engineering practices. The metadata and SHA-256 hashing could also be automated further so that every transformation step produces a fingerprint and an annotation file. Over time this becomes a complete provenance system where every dataset version is fully traceable.
Finally the project could benefit from deeper evaluation of model uncertainty, missing data patterns and data quality assessments. For example pollutant sensors sometimes malfunction or weather instruments may have calibration issues, and identifying those patterns could prevent misleading interpretations. Incorporating uncertainty estimates or confidence bands in visualizations could also make the findings stronger.
Overall there is a wide landscape of extensions that could make the project more robust, more predictive, more explainable and more aligned with real world environmental data science practices.
