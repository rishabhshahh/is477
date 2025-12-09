import hashlib
from pathlib import Path

cleaned_file = Path("data/cleaned/final_dataset_cleaned.csv")
results_dir = Path("results")
results_dir.mkdir(parents=True, exist_ok=True)
output_file = results_dir / "cleaned_sha256.txt"

sha256 = hashlib.sha256()
with open(cleaned_file, "rb") as f:
    for block in iter(lambda: f.read(4096), b""):
        sha256.update(block)

digest = sha256.hexdigest()

with open(output_file, "w") as f:
    f.write(digest + "\n")

print("Cleaned SHA-256:", digest)
