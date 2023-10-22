from pathlib import Path
from random import uniform
from typing import Union

import pandas as pd
from tqdm.contrib.itertools import product  # Same as `itertools.product`, but with a progress bar.


fake_json_path = Path.cwd() / "datasets" / "json"
fake_json = fake_json_path / "fake_data.json"
fake_parquet_path = Path.cwd() / "datasets" / "parquet"
fake_parquet = fake_parquet_path / "fake_data.parquet"

# Cached fake data
fake_data: pd.DataFrame | None = None
def generate_fake_data():
    """Generates 1_000_000 fake entity-attribute-value records."""

    global fake_data

    # Generate the data once.
    if fake_data is not None:
        return

    attributes = [f"attr_{i}" for i in range(100)]
    entities = [i for i in range(10_000)]

    temp_fake_data = [
        {"entity": e, "attr": a, "value": round(uniform(0, 10), 2)}
        for e, a in product(attributes, entities)
    ]

    fake_data = pd.DataFrame(temp_fake_data)


if not fake_json.exists():
    generate_fake_data()
    fake_json_path.mkdir(parents=True)
    fake_data.to_json(fake_json)


if not fake_parquet.exists():
    generate_fake_data()
    fake_parquet_path.mkdir(parents=True)
    fake_data.to_parquet(fake_parquet)
