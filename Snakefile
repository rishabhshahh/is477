RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
CLEANED_DIR = "data/cleaned"
SCRIPTS_DIR = "scripts"
RESULTS_DIR = "results"

# Final target: having the cleaned hash means everything before it ran
rule all:
    input:
        f"{RESULTS_DIR}/cleaned_sha256.txt"

rule hash_processed:
    input:
        f"{PROCESSED_DIR}/final_dataset.csv"
    output:
        f"{RESULTS_DIR}/processed_sha256.txt"
    shell:
        "python {SCRIPTS_DIR}/hash_processed.py"

rule clean_data:
    input:
        dataset=f"{PROCESSED_DIR}/final_dataset.csv",
        sha=f"{RESULTS_DIR}/processed_sha256.txt"
    output:
        f"{CLEANED_DIR}/final_dataset_cleaned.csv"
    shell:
        "python {SCRIPTS_DIR}/clean_data.py"

rule hash_cleaned:
    input:
        f"{CLEANED_DIR}/final_dataset_cleaned.csv"
    output:
        f"{RESULTS_DIR}/cleaned_sha256.txt"
    shell:
        "python {SCRIPTS_DIR}/hash_cleaned.py"
