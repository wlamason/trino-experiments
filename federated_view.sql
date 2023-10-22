-- run in dbeaver
drop table if exists pg1.public.customer;
drop table if exists pg2.public.nation;
drop table if exists mysql.tiny.region;

create table pg1.public.customer as
select * from tpch.tiny.customer limit 10;

create table pg2.public.nation as
select * from tpch.tiny.nation;

create table mysql.tiny.region as
select * from tpch.tiny.region;

describe pg1.public.customer;
describe pg2.public.nation;
describe mysql.tiny.region;

-- hive view
create view hive.default.test_view as
select c.name as customer_name, c.address, c.phone, n.name as nation, r.name as region
from pg1.public.customer c
join pg2.public.nation n
	on c.nationkey = n.nationkey
join mysql.tiny.region r
	on n.regionkey = r.regionkey;

show tables from hive.default;

select * from hive.default.test_view;

-- iceberg view
create view iceberg.default.test_view as
select c.name as customer_name, c.address, c.phone, n.name as nation, r.name as region
from pg1.public.customer c
join pg2.public.nation n
	on c.nationkey = n.nationkey
join mysql.tiny.region r
	on n.regionkey = r.regionkey;

show tables from iceberg.default;

select * from iceberg.default.test_view;
