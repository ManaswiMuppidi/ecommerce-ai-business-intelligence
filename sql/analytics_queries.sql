-- Revenue by category
SELECT category, SUM(revenue) AS revenue, SUM(profit) AS profit
FROM ecommerce_orders GROUP BY category ORDER BY revenue DESC;

-- Customer segment performance
SELECT customer_segment, COUNT(DISTINCT customer_id) AS customers,
SUM(revenue) AS revenue, AVG(revenue) AS avg_order_value
FROM ecommerce_orders GROUP BY customer_segment ORDER BY revenue DESC;

-- Window-function example
SELECT product, revenue,
RANK() OVER (ORDER BY revenue DESC) AS revenue_rank
FROM (
 SELECT product, SUM(revenue) AS revenue
 FROM ecommerce_orders GROUP BY product
) x;