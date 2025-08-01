-- Last updated: 8/1/2025, 6:27:31 PM
# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P LEFT JOIN Address A
on P.personId = A.personId