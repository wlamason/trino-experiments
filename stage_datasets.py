from pathlib import Path

import boto3
from tqdm import tqdm


CWD = Path.cwd()

s3 = boto3.client("s3", endpoint_url="http://localhost:9000", aws_access_key_id="minio", aws_secret_access_key="minio123")


# Upload every file in the datasets folder to the staging prefix except .gitkeep
for p in tqdm((CWD / "datasets").iterdir()):
    if p.name == ".gitkeep":
        continue
    relative_path = f"datasets/{p.name}"  # temporary until I migrate my wsl projects to the wsl filesystem instead of mnt
    s3.upload_file(Filename=relative_path, Bucket="datalake", Key=f"staging/{p.name}")
