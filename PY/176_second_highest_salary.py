# 176. Second Highest Salary Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 34213
# Total Submissions: 177653
# Difficulty: Easy
# Contributors: Admin
# Write a SQL query to get the second highest salary from the Employee table.
# 
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

# Write your MySQL query statement below
select
(
select distinct Salary
from Employee as e
order by Salary desc
limit 1, 1
) as SecondHighestSalary
