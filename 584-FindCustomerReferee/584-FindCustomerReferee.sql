-- Last updated: 8/1/2025, 6:26:29 PM
# Write your MySQL query statement below
SELECT name
FROM customer
WHERE referee_id != 2 OR referee_id IS NULL;