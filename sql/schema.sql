CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(4,2) NOT NULL,
    payment_method VARCHAR(40),
    city VARCHAR(60),
    order_status VARCHAR(30),
    revenue DECIMAL(12,2)
);
