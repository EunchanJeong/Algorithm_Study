-- 코드를 입력하세요
SELECT FO.product_id, FP.product_name, sum(FP.price * FO.amount) as total_sales
FROM FOOD_ORDER FO
JOIN FOOD_PRODUCT FP ON FO.product_id = FP.product_id
WHERE TO_CHAR(FO.produce_date, 'YYYY-MM') = '2022-05'
GROUP BY FO.product_id, FP.product_name
ORDER BY total_sales DESC, product_id ASC;