-- run in dbeaver
drop table if exists pg1.public.customer;
drop table if exists pg2.public.nation;
drop table if exists mysql.tiny.region;

show schemas from tpch;
show tables from tpch.tiny;

select * from tpch.tiny.customer limit 10;
select * from tpch.tiny.nation limit 10;
select * from tpch.tiny.region limit 10;

select *
from tpch.tiny.customer c
join tpch.tiny.nation n
	on c.nationkey = n.nationkey 
limit 10;

describe tpch.tiny.customer;

-- CREATE TABLE pg1.public.customer (
--     custkey	    bigint,
--     name	    varchar(25),
--     address	    varchar(40),
--     nationkey	bigint,
--     phone	    varchar(15),
--     acctbal	    double,
--     mktsegment	varchar(10),
--     comment	    varchar(117)
-- );

show create table tpch.tiny.customer;
-- SHOW CREATE table tpch.tiny.customer;
-- CREATE TABLE pg1.public.customer (
--    custkey bigint NOT NULL,
--    name varchar(25) NOT NULL,
--    address varchar(40) NOT NULL,
--    nationkey bigint NOT NULL,
--    phone varchar(15) NOT NULL,
--    acctbal double NOT NULL,
--    mktsegment varchar(10) NOT NULL,
--    comment varchar(117) NOT NULL
-- );

create table pg1.public.customer as
select * from tpch.tiny.customer limit 10;

select * from pg1.public.customer;

create table pg2.public.nation as
select * from tpch.tiny.nation;

select * from  pg2.public.nation;
	
create table mysql.tiny.region as
select * from tpch.tiny.region;

select * from mysql.tiny.region;

select *
from pg1.public.customer c
join pg2.public.nation n
	on c.nationkey = n.nationkey 
join mysql.tiny.region r
	on n.regionkey = r.regionkey;