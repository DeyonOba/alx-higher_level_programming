-- Script that displays the top 3 cities temperature during July and August ordered
-- temperature (descending)
SELECT city, AVG(value) as avg_temp
    FROM temperatures 
    WHERE month BETWEEN 7 AND 8
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;