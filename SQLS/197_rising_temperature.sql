# 197. Rising Temperature Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 26312 Total Submissions: 99390 Difficulty: Easy
# Contributor: LeetCode
# Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
# 
# +---------+------------+------------------+
# | Id(INT) | Date(DATE) | Temperature(INT) |
# +---------+------------+------------------+
# |       1 | 2015-01-01 |               10 |
# |       2 | 2015-01-02 |               25 |
# |       3 | 2015-01-03 |               20 |
# |       4 | 2015-01-04 |               30 |
# +---------+------------+------------------+
# For example, return the following Ids for the above Weather table:
# +----+
# | Id |
# +----+
# |  2 |
# |  4 |
# +----+





























#2017.03.31 

SELECT w1.Id
FROM Weather w1, Weather w2
WHERE 
  w1.Temperature > w2.Temperature
  AND DATEDIFF(w1.Date, w2.Date) = 1
