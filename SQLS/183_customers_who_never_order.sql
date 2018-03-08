/* # 183. Customers Who Never Order Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 31312 Total Submissions: 102389 Difficulty: Easy
# Contributor: LeetCode
# Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.
# 
# Table: Customers.
# 
# +----+-------+
# | Id | Name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Table: Orders.
# 
# +----+------------+
# | Id | CustomerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# Using the above tables as example, return the following:
# 
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+ */



-- 2018.03.07
SELECT Name AS Customers
FROM Customers c
WHERE 
  c.id NOT IN (SELECT DISTINCT CustomerId FROM Orders o)






































# 2017.03.31
SELECT name as Customers
FROM Customers c
WHERE c.id not IN (SELECT CustomerId FROM Orders)
