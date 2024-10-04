-- 코드를 입력하세요
SELECT ingredient_type, SUM(total_order) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.flavor = I.flavor
GROUP BY ingredient_type
ORDER BY TOTAL_ORDER ASC;