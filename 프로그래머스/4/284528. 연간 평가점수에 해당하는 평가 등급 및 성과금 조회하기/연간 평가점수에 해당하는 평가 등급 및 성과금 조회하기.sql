SELECT  HG.EMP_NO,
        EMP_NAME,
        CASE 
            WHEN SUM(SCORE)/2 >= 96 THEN 'S'
            WHEN SUM(SCORE)/2 >= 90 THEN 'A'
            WHEN SUM(SCORE)/2 >= 80 THEN 'B'
            ELSE 'C'
            END AS "GRADE",
        CASE 
            WHEN SUM(SCORE)/2 >= 96 THEN SAL * (0.2)
            WHEN SUM(SCORE)/2 >= 90 THEN SAL * (0.15)
            WHEN SUM(SCORE)/2 >= 80 THEN SAL * (0.1)
            ELSE 0
            END AS "BONUS"
FROM HR_GRADE HG
LEFT JOIN HR_EMPLOYEES HE ON HG.EMP_NO = HE.EMP_NO
GROUP BY HG.EMP_NO, YEAR
ORDER BY EMP_NO ASC;