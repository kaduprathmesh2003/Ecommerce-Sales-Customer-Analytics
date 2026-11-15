USE ecommerce_analytics;

-- Delivered sales KPIs
SELECT COUNT(DISTINCT order_id) AS delivered_orders,
       ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS delivered_revenue
FROM orders WHERE order_status = 'Delivered';

-- Monthly revenue
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS revenue
FROM orders WHERE order_status = 'Delivered'
GROUP BY DATE_FORMAT(order_date, '%Y-%m') ORDER BY month;

-- Category performance
SELECT category, ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS revenue,
       COUNT(DISTINCT order_id) AS orders
FROM orders WHERE order_status = 'Delivered'
GROUP BY category ORDER BY revenue DESC;

-- Top customers
SELECT customer_id, ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS spend,
       COUNT(DISTINCT order_id) AS orders
FROM orders WHERE order_status = 'Delivered'
GROUP BY customer_id ORDER BY spend DESC LIMIT 10;

-- Order status mix
SELECT order_status, COUNT(*) AS order_lines
FROM orders GROUP BY order_status ORDER BY order_lines DESC;

-- City performance
SELECT city, ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS revenue
FROM orders WHERE order_status = 'Delivered'
GROUP BY city ORDER BY revenue DESC;
