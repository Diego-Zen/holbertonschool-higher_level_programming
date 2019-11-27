-- Lists all cities
SELECT ci.id, ci.name, st.name
FROM cities AS ci
INNER JOIN states AS st ON st.id = ci.state_id;
