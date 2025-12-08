import hashlib

file_path = "final_dataset_uncleaned.csv"

sha256_hash = hashlib.sha256()

with open(file_path, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

print("SHA-256:", sha256_hash.hexdigest())
