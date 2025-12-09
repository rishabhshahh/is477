import hashlib
from pathlib import Path

file_path = Path("data/cleaned/ffinal_dataset_cleaned.csv")  # update name if different

sha256 = hashlib.sha256()

with open(file_path, "rb") as f:
    for block in iter(lambda: f.read(4096), b""):
        sha256.update(block)

print("Cleaned SHA-256:", sha256.hexdigest())
