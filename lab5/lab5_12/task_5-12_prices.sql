--1
select prduct_id, count(*) from prices group by prduct_id order by prduct_id asc;
--2
select prduct_id, avg(price) from prices group by prduct_id order by prduct_id asc;
--3
select prduct_id, min(price) from prices group by prduct_id order by prduct_id asc;
--4
select prduct_id, max(price) from prices group by prduct_id order by prduct_id asc;
