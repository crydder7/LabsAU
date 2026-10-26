--1
select category,count(*) from products group by category;
--2
select category,count(*) from products group by category order by count(*) desc;
