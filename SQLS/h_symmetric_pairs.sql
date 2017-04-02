/*
Symmetric Pairs 
by AvimanyuSingh
Problem
Submissions
Leaderboard
Discussions
You are given a table, Functions, containing two columns: X and Y. Y is the value of some function F at X -- i.e. Y = F(X).



Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X.

Sample Input



Sample Output

20 20
20 21
22 23
*/

select distinct f1.x, f1.y
from 
    functions f1, 
    functions f2
where (f1.x = f2.y and f1.y = f2.x and f1.x < f1.y)
      or (f1.x = f1.y and (select count(*) cn from functions f3 where f1.x = f3.x and f1.y = f3.y) > 1)
order by f1.x
