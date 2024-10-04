-- 코드를 입력하세요
SELECT C.car_type, COUNT(C.car_type) AS CARS
FROM car_rental_company_car C
WHERE C.options LIKE '%통풍시트%' OR C.options LIKE '%열선시트%' OR C.options LIKE '%가죽시트%'
GROUP BY C.car_type
ORDER BY C.car_type;