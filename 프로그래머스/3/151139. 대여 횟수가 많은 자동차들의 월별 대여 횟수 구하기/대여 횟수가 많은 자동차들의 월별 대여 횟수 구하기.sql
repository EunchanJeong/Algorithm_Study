-- 코드를 입력하세요
SELECT TO_NUMBER(TO_CHAR(start_date, 'MM')) AS MONTH, car_id, COUNT(history_id) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE TO_CHAR(start_date, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
    AND car_id in (
                    SELECT car_id
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    WHERE TO_CHAR(start_date, 'YYYY-MM') BETWEEN '2022-08' AND '2022-10'
                    GROUP BY car_id
                    HAVING COUNT(history_id) >= 5)
GROUP BY TO_CHAR(start_date, 'MM'), car_id
HAVING COUNT(history_id) > 0
ORDER BY MONTH ASC, car_id DESC;