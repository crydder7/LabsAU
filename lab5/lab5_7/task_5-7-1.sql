CREATE TABLE IF NOT EXISTS products (

    id SERIAL primary key,

    name VARCHAR(100) not null,

    category VARCHAR(50)
);




CREATE TABLE IF NOT EXISTS prices (

    id SERIAL PRIMARY key,

    prduct_id INTEGER REFERENCES products(id),
	
    price numeric(10,2) not null,
    
    created_at timestamp DEFAULT current_timestamp

);




CREATE TABLE IF NOT EXISTS enrollments (

    id SERIAL primary KEY,

    name varchar(100) not null,

    product_id integer references products(id)

);

select * FROM products p JOIN prices pr;