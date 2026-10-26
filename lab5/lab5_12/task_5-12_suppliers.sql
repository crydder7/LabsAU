--1
select product_id, count(product_id) from enrollments group by product_id order by product_id asc;