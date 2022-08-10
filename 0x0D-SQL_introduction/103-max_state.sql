-- Display max temp of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
ORDER BY state
LIMIT 3;
