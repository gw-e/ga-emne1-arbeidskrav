-- 1. Produktoversikt:

SELECT product_name, category, price, stock
FROM products
WHERE price > 750
  AND stock > 10
ORDER BY price DESC;


-- 2. Kunder i utvalgte byer;

SELECT *
FROM customers
WHERE city in ('Oslo', 'Bergen', 'Trondheim')
ORDER BY city, last_name;


-- 3. Bestillinger i en periode:

SELECT *
FROM orders
WHERE order_date >= '2025-07-01'
  AND order_date < '2025-08-01';


-- 4. Full bestillingsoversikt:

SELECT
    orders.order_id,
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    products.price,
    orders.order_date,
    orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
ORDER BY orders.order_id;


-- 5. Beregnet verdi:

SELECT
    orders.order_id,
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    products.price,
    orders.quantity * products.price AS total_price,
    orders.order_date,
    orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
ORDER BY orders.order_id;


-- 6. Bestillinger med høy verdi:

SELECT
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    products.price,
    orders.quantity * products.price AS total_price
FROM orders
JOIN customers
    ON orders.customer_id = customers.customer_id
JOIN products
    ON orders.product_id = products.product_id
WHERE orders.quantity * products.price > 2000
ORDER BY total_price DESC;


-- 7. Bestillinger per status:

SELECT status, COUNT(order_id) AS statusCount
FROM orders
GROUP BY status;


