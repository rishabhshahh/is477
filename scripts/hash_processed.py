import hashlib
from pathlib import Path

file_path = Path("data/processed/final_dataset.csv")

sha256 = hashlib.sha256()

with open(file_path, "rb") as f:
    for block in iter(lambda: f.read(4096), b""):
        sha256.update(block)

print("Processed SHA-256:", sha256.hexdigest())
