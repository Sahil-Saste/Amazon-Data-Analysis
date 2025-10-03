-- Amazon Sales Analysis SQL Queries

-- 1. Sales Overview (Monthly revenue trends)
SELECT 
    strftime('%Y-%m', Date) AS Month,
    SUM(Amount) AS Total_Revenue
FROM amazon_sales
GROUP BY Month
ORDER BY Month;

-- 2. Top Products (by revenue)
SELECT 
    SKU,
    SUM(Amount) AS Total_Revenue,
    SUM(Qty) AS Total_Quantity
FROM amazon_sales
GROUP BY SKU
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 3. Fulfillment Analysis (orders by fulfillment method)
SELECT 
    Fulfilment,
    COUNT(Order_ID) AS Total_Orders,
    SUM(Amount) AS Total_Revenue
FROM amazon_sales
GROUP BY Fulfilment
ORDER BY Total_Revenue DESC;

-- 4. Geographical Sales (state-wise revenue)
SELECT 
    Ship_State,
    SUM(Amount) AS Total_Revenue,
    COUNT(Order_ID) AS Total_Orders
FROM amazon_sales
GROUP BY Ship_State
ORDER BY Total_Revenue DESC;

-- 5. Customer Segmentation (based on total spend)
SELECT 
    Buyer_Name,
    SUM(Amount) AS Total_Spend,
    CASE 
        WHEN SUM(Amount) > 50000 THEN 'High Value'
        WHEN SUM(Amount) BETWEEN 10000 AND 50000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Customer_Segment
FROM amazon_sales
GROUP BY Buyer_Name
ORDER BY Total_Spend DESC;
