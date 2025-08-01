-- Last updated: 8/1/2025, 6:26:01 PM
# Write your MySQL query statement below
SELECT 
    query_name ,
    ROUND(AVG(rating/position),2) AS quality , 
    ROUND(AVG(rating<3)*100,2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;