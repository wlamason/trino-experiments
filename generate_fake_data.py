from pathlib import Path
from random import uniform
from typing import Union

import pandas as pd
from tqdm.contrib.itertools import product  # Same as `itertools.product`, but with a progress bar.


fake_csv_path = Path.cwd() / "datasets" / "csv"
fake_csv = fake_csv_path / "fake_data.csv"
fake_json_path = Path.cwd() / "datasets" / "json"
fake_json = fake_json_path / "fake_data.json"
fake_parquet_path = Path.cwd() / "datasets" / "parquet"
fake_parquet = fake_parquet_path / "fake_data.parquet"

# Cached fake data
_fake_data: pd.DataFrame | None = None
def generate_fake_data() -> pd.DataFrame:
    """Generates 1_000_000 fake entity-attribute-value records."""

    global _fake_data

    # Generate the data once.
    if _fake_data is not None:
        return _fake_data

    attributes = [f"attr_{i}" for i in range(100)]
    entities = [i for i in range(10_000)]

    temp_fake_data = [
        {"entity": e, "attr": a, "value": round(uniform(0, 10), 2)}
        for e, a in product(entities, attributes)
    ]

    _fake_data = pd.DataFrame.from_records(temp_fake_data)
    return _fake_data


if not fake_csv.exists():
    fake_data = generate_fake_data()
    fake_csv_path.mkdir(parents=True)
    fake_data.to_csv(fake_csv, index=False)


if not fake_json.exists():
    fake_data = generate_fake_data()
    fake_json_path.mkdir(parents=True)
    fake_data.to_json(fake_json, orient="records", lines=True)


if not fake_parquet.exists():
    fake_data = generate_fake_data()
    fake_parquet_path.mkdir(parents=True)
    fake_data.to_parquet(fake_parquet)
