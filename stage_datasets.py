from os import walk
from pathlib import Path

import boto3
from tqdm import tqdm


DATASETS_DIR = Path.cwd() / "datasets"

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minio",
    aws_secret_access_key="minio123",
)


# Upload every file in the datasets folder to the staging prefix except .gitkeep
for root, dirs, files in tqdm(walk(DATASETS_DIR)):  # Can switch to DATASETS_DIR.walk() in py3.12
    for f in files:
        f = Path(f)  # Can remove the Path wrap in py3.12
        if f.name == ".gitkeep":
            continue

        absolute_file_path = Path(root) / f  # Can remove the Path wrap in py3.12

        rel_path = absolute_file_path.relative_to(DATASETS_DIR)
        s3.upload_file(
            Filename=absolute_file_path, Bucket="datalake", Key=f"staging/{rel_path}"
        )
