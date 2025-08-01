-- Last updated: 8/1/2025, 6:26:26 PM
# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE
  MOD(id, 2) = 1
  AND description != 'boring'
ORDER BY rating DESC