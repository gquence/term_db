select P.*, T_I.name AS team_name 
    from projects P 
         JOIN 
         team_info T_I 
         ON T_I.id_team = P.id_team
where T_I.name = :team_name AND status <> 'success' AND status <> 'failure' AND deadline >= CURRENT_DATE;