import hashlib
from pathlib import Path

processed_file = Path("data/processed/final_dataset.csv")
results_dir = Path("results")
results_dir.mkdir(parents=True, exist_ok=True)
output_file = results_dir / "processed_sha256.txt"

sha256 = hashlib.sha256()
with open(processed_file, "rb") as f:
    for block in iter(lambda: f.read(4096), b""):
        sha256.update(block)

digest = sha256.hexdigest()

with open(output_file, "w") as f:
    f.write(digest + "\n")

print("Processed SHA-256:", digest)
