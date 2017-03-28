# 177. Nth Highest Salary Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 17413
# Total Submissions: 109453
# Difficulty: Medium
# Contributors: Admin
# Write a SQL query to get the nth highest salary from the Employee table.
# 
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee order by Salary desc limit N, 1
  );
END
