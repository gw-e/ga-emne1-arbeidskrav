-- OPPGAVE 3:
-------------

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
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE orders.quantity * products.price > 2000
ORDER BY total_price DESC;


-- 7. Bestillinger per status:

SELECT status, COUNT(order_id) AS statusCount
FROM orders
GROUP BY status;


-- 8. Gjennomsnittspris per kategori:

SELECT category, AVG(price) AS AvgPrice
FROM products
GROUP BY category
ORDER BY AvgPrice DESC;


-- 9. Bestillinger per kunde:

SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    COUNT(orders.order_id) AS ordersCount
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.first_name, customers.last_name
ORDER BY ordersCount DESC;


-- 10. Antall solgte produkter:

SELECT
    products.product_id,
    products.product_name,
    SUM(orders.quantity) AS ordersAmount
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
GROUP BY products.product_id, products.product_name
ORDER BY ordersAmount DESC;


-- 11. Beregnet verdi per produkt:

SELECT
    products.product_name,
    COALESCE(SUM(orders.quantity), 0) AS amountOrdered,
    COALESCE(SUM(orders.quantity * products.price), 0) AS totalPrice
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
GROUP BY products.product_id, products.product_name
ORDER BY totalPrice DESC;


-- 12. Kunder med flere bestillinger:

SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    COUNT(orders.order_id) ordersPerCostumer
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY
    customers.customer_id,
    customers.first_name,
    customers.last_name
HAVING ordersPerCostumer > 1
ORDER BY ordersPerCostumer DESC;


-- 13. Kunder uten bestillinger: 

SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;


-- 14. Produkter uten bestillinger:

SELECT products.product_id, products.product_name
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
WHERE orders.order_id IS NULL;


-- 15. Utforskingsoppgave:

SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    SUM(orders.quantity * products.price) AS totalPrice
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN products ON orders.product_id = products.product_id
GROUP BY
    customers.customer_id,
    customers.first_name,
    customers.last_name
ORDER BY totalPrice DESC
LIMIT 1;

-- Jeg koblet sammen customers, orders og products ved hjelp av JOIN for å hente kundeinformasjon,
-- bestilte mengder og produktpriser. Deretter brukte jeg SUM(orders.quantity * products.price) for
-- å finne ut summen av bestillingene for hver kunde. Jeg grupperte derretter resultatene med GROUP BY
-- per kunde og sorterte dem med ORDER BY slik at kunden med høyest samlet verdi kom først.
-- Til slutt brukte jeg LIMIT 1 for å bare vise den med høyest sum.



-- OPPGAVE 4:
-------------

-- 1. Registrer en ny kunde:

INSERT INTO customers (first_name, last_name, email, city, registered_date)
VALUES ('Henrik', 'Solberg', 'henrik.solberg@example.com', 'Lillehammer', '2026-10-22');

SELECT *
FROM customers
WHERE email = 'henrik.solberg@example.com';


-- 2. Registrer flere produkter:

INSERT INTO products (product_name, category, price, stock)
VALUES
    ('USB-C cable', 'Accessories', 199, 50),
    ('Docking station', 'Accessories', 1899, 12),
    ('External SSD 2TB', 'Storage', 1999, 8);

SELECT *
FROM products;


-- 3. Registrer nye bestillinger: 

SELECT customer_id
FROM customers
WHERE first_name = 'Henrik'
  AND last_name = 'Solberg';
-- Output: 9

SELECT product_id, product_name
FROM products
WHERE product_name IN (
    'Docking station',
    'USB-C cable',
    'External SSD 2TB'
);
-- 11: USB-C cable
-- 12: Docking station
-- 13: External SSD 2TB

INSERT INTO orders
    (customer_id, product_id, quantity, order_date, status)
VALUES
    (9, 12, 1, '2026-10-22', 'Processing'),
    (9, 11, 2, '2026-10-22', 'Processing'),
    (9, 13, 1, '2026-10-22', 'Processing');

SELECT
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    orders.order_date,
    orders.status
FROM orders
JOIN customers
    ON orders.customer_id = customers.customer_id
JOIN products
    ON orders.product_id = products.product_id
WHERE customers.customer_id = 9;


-- 4. Prisendring:

SELECT product_id, product_name, price
FROM products
WHERE category = 'Accessories';

UPDATE products
SET price = price * 1.08
WHERE category = 'Accessories';

SELECT product_id, product_name, price
FROM products
WHERE category = 'Accessories';


-- 5. Lagerpåfylling:

SELECT *
FROM products
WHERE stock < 15;

UPDATE products
SET stock = stock + 20
WHERE stock < 15;


-- 6. Endre flere verdier:

SELECT *
FROM products
WHERE product_name = 'Gaming headset';
-- id: 7

UPDATE products
SET price = price * 1.15,
    stock = stock + 10
WHERE product_id = 7;


-- 7. Oppdater ordrestatus:

SELECT *
FROM orders
WHERE status = 'Shipped'
  AND order_date < '2025-08-10';

UPDATE orders
SET status = 'Delivered'
WHERE status = 'Shipped'
  AND order_date < '2025-08-10';

SELECT *
FROM orders
WHERE status = 'Delivered'
  AND order_date < '2025-08-10';


-- 8. Opprett og slett testdata:

-- legg til dataen

INSERT INTO customers
    (first_name, last_name, email, city, registered_date)
VALUES
    ('Test', 'Customer', 'testcustomer@example.com','Oslo', CURDATE());

INSERT INTO products
    (product_name, category, price, stock)
VALUES
    ('Test Product', 'Accessories', 100.00, 10);

SELECT customer_id
FROM customers
WHERE first_name = 'Test'
  AND last_name = 'Customer';
-- customer_id : 10

SELECT product_id
FROM products
WHERE product_name = 'Test Product';
-- product_id: 14

INSERT INTO orders
    (customer_id, product_id, quantity, order_date, status)
VALUES
    (10, 14, 1, CURDATE(), 'Processing');

-- kontroller at dataen ble laget

SELECT
    customers.first_name,
    customers.last_name,
    products.product_name,
    orders.quantity,
    orders.order_date,
    orders.status
FROM orders
JOIN customers
    ON orders.customer_id = customers.customer_id
JOIN products
    ON orders.product_id = products.product_id
WHERE customers.email = 'testcustomer@example.com'
  AND products.product_name = 'Test Product';

-- 1. Slett bestillingen først fordi den refererer til kunden og produktet med fremmednøkler.
DELETE FROM orders
WHERE customer_id = 10
  AND product_id = 14;

-- 2. Deretter slett produktet fordi bestillingen ikke lenger refererer til produktet.
DELETE FROM products
WHERE product_id = 14;

-- 3. Deretter slett kunden fordi bestillingen ikke lenger refererer til kunden.
DELETE FROM customers
WHERE customer_id = 10;


-- 9: Bruk en transaksjon:

-- Velger en random kunde
SELECT *
FROM customers;
-- id: 7

-- Velger et random produkt
SELECT *
FROM products;
-- id: 5

START TRANSACTION;

INSERT INTO orders
    (customer_id, product_id, quantity, order_date, status)
VALUES
    (7, 5, 1, CURDATE(), 'Processing');

UPDATE products
SET stock = stock - 1
WHERE product_id = 5;

SELECT *
FROM orders
WHERE customer_id = 10
  AND product_id = 5
ORDER BY order_id DESC
LIMIT 1;

SELECT *
FROM products
WHERE product_id = 5;

COMMIT;

-- COMMIT lagrer begge endringene permanent.
-- ROLLBACK angre begge endringene dersom COMMIT ikke er kjørt.
-- Transaksjoner gjør at relaterte endringer behandles samlet og samtidig,
-- slik at bestillingen og lagerbeholdningen forblir konsistente
-- og man unngår feil ved spørringer eller endringer som skjer
-- imellom de relaterte endringene.
