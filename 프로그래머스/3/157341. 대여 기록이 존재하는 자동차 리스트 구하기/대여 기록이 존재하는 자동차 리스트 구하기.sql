SELECT DISTINCT(CH.CAR_ID)
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
INNER JOIN CAR_RENTAL_COMPANY_CAR CC ON CH.CAR_ID = CC.CAR_ID
WHERE CC.CAR_TYPE = '세단' AND TO_CHAR(CH.START_DATE, 'MM') = 10
ORDER BY CH.CAR_ID DESC;
