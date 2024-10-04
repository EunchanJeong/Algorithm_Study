SELECT A.GRADE, A.ID, A.EMAIL
FROM (SELECT CASE WHEN (ID, 'Python') IN (SELECT B.ID, A.NAME
                FROM SKILLCODES  A RIGHT JOIN DEVELOPERS  B
                ON A.CODE & B.SKILL_CODE)
                AND (ID, 'Front End') IN (SELECT B.ID, A.CATEGORY
                FROM SKILLCODES  A RIGHT JOIN DEVELOPERS  B
                ON A.CODE & B.SKILL_CODE) 
            THEN 'A'
            ELSE CASE WHEN (ID, 'C#') IN (SELECT B.ID, A.NAME
                                            FROM SKILLCODES  A RIGHT JOIN DEVELOPERS  B
                                            ON A.CODE & B.SKILL_CODE)
                      THEN 'B'
                      ELSE CASE WHEN (ID, 'Front End') IN (SELECT B.ID, A.CATEGORY
                                    FROM SKILLCODES  A RIGHT JOIN DEVELOPERS  B
                                    ON A.CODE & B.SKILL_CODE)
                                THEN 'C'
                                ELSE NULL
                            END
                END
        END GRADE, ID, EMAIL
FROM DEVELOPERS) A
WHERE A.GRADE IS NOT NULL
ORDER BY A.GRADE, A.ID;