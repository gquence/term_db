SELECT DISTINCT I1.*
FROM instrument I1 
    LEFT  JOIN 
    (
        SELECT DISTINCT I.id_instrument 
        FROM projects P 
            INNER JOIN
            instrument I
                ON (P.status = 'in_progress' OR P.status='waiting')
                AND I.usability='t' AND P.id_instrument = I.id_instrument
    )
    AS x 
    ON I1.id_instrument = x.id_instrument 
WHERE x.id_instrument IS NULL;