/*
# 180. Consecutive Numbers Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 16097 Total Submissions: 70714 Difficulty: Medium
# Contributor: LeetCode
# Write a SQL query to find all numbers that appear at least three times consecutively.
# 
# +----+-----+
# | Id | Num |
# +----+-----+
# | 1  |  1  |
# | 2  |  1  |
# | 3  |  1  |
# | 4  |  2  |
# | 5  |  1  |
# | 6  |  2  |
# | 7  |  2  |
# +----+-----+
# For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.
# 
# Subscribe to see which companies asked this question.
*/



-- 2018.03.07
SELECT DISTINCT sub.Num AS ConsecutiveNums
FROM (
    SELECT
        l.Num,
        @lastNum AS c1,
        @lastTwoNum AS c2,
        @lastTwoNum := @lastNum,
        @lastNum := Num
    FROM
        logs l,
        (SELECT @lastNum := null, @lastTwoNum := null) v
) sub
WHERE sub.Num = sub.c1 AND sub.Num = sub.c2



















# 2017.03.31 
SELECT DISTINCT l1.num ConsecutiveNums 
FROM
    Logs l1 
JOIN Logs l2 on l1.Id - l2.Id = 1
JOIN Logs l3 on l2.Id - l3.Id = 1
WHERE l1.Num = l2.Num
  AND l2.Num = l3.Num
