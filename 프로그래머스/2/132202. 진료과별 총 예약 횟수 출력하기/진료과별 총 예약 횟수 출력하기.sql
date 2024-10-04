SELECT mcdp_cd AS "진료과코드", COUNT(pt_no) AS "5월 예약건수"
FROM APPOINTMENT
WHERE TO_CHAR(apnt_ymd, 'YYYY-MM') = '2022-05'
GROUP BY mcdp_cd
ORDER BY "5월 예약건수" ASC, mcdp_cd ASC;