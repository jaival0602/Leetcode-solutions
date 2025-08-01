-- Last updated: 8/1/2025, 6:25:33 PM
# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15