CREATE TABLE ecommerce_orders (
 order_id BIGINT PRIMARY KEY, order_date DATE, customer_id INT,
 region VARCHAR(20), customer_segment VARCHAR(30), channel VARCHAR(30),
 category VARCHAR(30), product VARCHAR(60), quantity INT,
 unit_price DECIMAL(12,2), discount_pct DECIMAL(6,2),
 revenue DECIMAL(14,2), cost DECIMAL(14,2), profit DECIMAL(14,2),
 returned BOOLEAN, satisfaction_score DECIMAL(3,1), delivery_days DECIMAL(4,1)
);