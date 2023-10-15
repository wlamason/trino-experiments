import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('trino://trino@localhost:8080/')
conn = engine.connect()

sql_select = "select * from tpch.tiny.customer limit 10"
df = pd.read_sql(sql_select, conn, dtype_backend="pyarrow")

sql_join = """
select *
from tpch.tiny.customer c
join tpch.tiny.nation n
    on c.nationkey = n.nationkey 
limit 10
"""
df = pd.read_sql(sql_join, conn, dtype_backend="pyarrow")
