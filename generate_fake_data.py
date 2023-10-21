# from itertools import product
from pathlib import Path
from random import uniform
from typing import Union

import pandas as pd
from tqdm.contrib.itertools import product  # Same as `itertools.product`, but with a progress bar.


CWD = Path.cwd()
fake_json = CWD / "datasets" / "fake_data.json"
fake_parquet = CWD / "datasets" / "fake_data.parquet"
fake_data: Union[pd.DataFrame, None] = None


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
    fake_data.to_json(fake_json)


if not fake_parquet.exists():
    generate_fake_data()
    fake_data.to_parquet(fake_parquet)
