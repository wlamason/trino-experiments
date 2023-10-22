-- Trino datatypes
-- https://trino.io/docs/current/language/types.html#

drop table hive.default.fake_csv_data;
create table hive.default.fake_csv_data (
    entity  VARCHAR,    -- Variable length character data with an optional maximum length.
    attr    VARCHAR,    -- Variable length character data with an optional maximum length.
    value   VARCHAR     -- Variable length character data with an optional maximum length.
)
WITH (
    format = 'CSV', -- The catalog property hive.storage-format sets the default value.
    skip_header_line_count = 1,
    external_location = 's3a://datalake/staging/csv/'
);

drop table hive.default.fake_json_data;
create table hive.default.fake_json_data (
    entity  INTEGER,    -- A 32-bit signed two’s complement integer with a minimum value of -2^31 or -0x80000000 and a maximum value of 2^31 - 1 or 0x7FFFFFFF.
    attr    VARCHAR,    -- Variable length character data with an optional maximum length.
    value   DOUBLE      -- A double is a 64-bit inexact, variable-precision implementing the IEEE Standard 754 for Binary Floating-Point Arithmetic.
)
WITH (
    format = 'JSON', -- The catalog property hive.storage-format sets the default value.
    external_location = 's3a://datalake/staging/json/'
);

drop table hive.default.fake_parquet_data;
create table hive.default.fake_parquet_data (
    entity  INTEGER,    -- A 32-bit signed two’s complement integer with a minimum value of -2^31 or -0x80000000 and a maximum value of 2^31 - 1 or 0x7FFFFFFF.
    attr    VARCHAR,    -- Variable length character data with an optional maximum length.
    value   DOUBLE      -- A double is a 64-bit inexact, variable-precision implementing the IEEE Standard 754 for Binary Floating-Point Arithmetic.
)
WITH (
    format = 'PARQUET', -- The catalog property hive.storage-format sets the default value.
    external_location = 's3a://datalake/staging/parquet/'
);

select * from hive.default.fake_csv_data limit 10;
select * from hive.default.fake_json_data limit 10;
select * from hive.default.fake_parquet_data limit 10;

select count(*) from hive.default.fake_csv_data;
select count(*) from hive.default.fake_json_data;
select count(*) from hive.default.fake_parquet_data;
