SELECT AO.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AI
INNER JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY (AO.DATETIME - AI.DATETIME + 1) DESC
FETCH FIRST 2 ROWS ONLY;