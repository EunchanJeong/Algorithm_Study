SELECT B.category, SUM(BS. sales) AS TOTAL_SALES
FROM BOOK_SALES BS
LEFT JOIN BOOK B ON BS.book_id = B.book_id
WHERE TO_CHAR(sales_date, 'YYYY-MM') = '2022-01'
GROUP BY category
ORDER BY category ASC;