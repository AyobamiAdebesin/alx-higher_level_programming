-- Display city by temperature
SELECT city, AVG(value) as avg_temp
FROM second_table
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
