# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) AS unit 
FROM products p join orders o
ON p.product_id = o.product_id
WHERE o.order_date BETWEEN "2020-02-01" AND "2020-02-29"
GROUP BY p.product_id, p.product_name
HAVING unit >= 100;