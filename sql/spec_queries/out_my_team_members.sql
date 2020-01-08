SELECT E.*, T_M.role, T_I.name AS team_name 
FROM employees E INNER JOIN team_members T_M ON E.id_employee = T_M.id_employee JOIN team_info T_I ON T_I.name = :team_name
ORDER BY role;
