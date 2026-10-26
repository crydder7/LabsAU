--1
select * from products where category = 'Электроника';
--2
select * from products where category = 'Одежда' and name like '%женская%';
--3
select * from products where category = 'Продукты' or category = 'Книги';
--4
select * from products where not category = 'Бытовая техника';
--5
select * from products p where category in ('Электроника','Одежда','Книги');
--6
select * from products where (category = 'Электроника' and name like '%Samsung%') or (category = 'Бытовая техника');
--7
select * from products where (category in ('Электроника','Бытовая техника','Одежда') and (id between 1 and 15) and name not like '%Samsung%') or category = 'Книги';