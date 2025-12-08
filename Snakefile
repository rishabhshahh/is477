RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
SCRIPTS_DIR = "scripts"
RESULTS_DIR = "results"

rule all:
    input:
        f"{PROCESSED_DIR}/final_dataset.csv"

rule clean_data:
    input:
        f"{PROCESSED_DIR}/final_dataset_uncleaned.csv"
    output:
        f"{PROCESSED_DIR}/final_dataset.csv"
    shell:
        "python {SCRIPTS_DIR}/clean_data.py"
