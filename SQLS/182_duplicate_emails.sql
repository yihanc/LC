/*# 182. Duplicate Emails Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 34940 Total Submissions: 94897 Difficulty: Easy
# Contributor: LeetCode
# Write a SQL query to find all duplicate emails in a table named Person.
# 
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# For example, your query should return the following for the above table:
# 
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# Note: All emails are in lowercase.
# 
# */ 


-- 2018.04.06 No subquery
SELECT Email
FROM Person a
GROUP BY EMAIL
HAVING COUNT(Email) > 1

-- 2018.03.07
SELECT sub.Email
FROM (
    SELECT 
      Email, 
      count(*) as cnt
    FROM Person p
    GROUP BY Email
    HAVING cnt > 1
) sub






-- 2017.04.07
select Email
from Person
group by Email
having count(email) > 1


-- 2017.04.07
select distinct p1.email as Email
from person p1, person p2
where p1.email = p2.email and p1.id > p2.id


-- 2017.04.01
select 
    tmp.email Email
from 
    ( select email, count(email) cn
    from person
    group by email
    having cn > 1 ) tmp
