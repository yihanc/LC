/*# 262. Trips and Users Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 9625 Total Submissions: 60548 Difficulty: Hard
# Contributor: LeetCode
# The Trips table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).
# 
# +----+-----------+-----------+---------+--------------------+----------+
# | Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
# +----+-----------+-----------+---------+--------------------+----------+
# | 1  |     1     |    10     |    1    |     completed      |2013-10-01|
# | 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
# | 3  |     3     |    12     |    6    |     completed      |2013-10-01|
# | 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
# | 5  |     1     |    10     |    1    |     completed      |2013-10-02|
# | 6  |     2     |    11     |    6    |     completed      |2013-10-02|
# | 7  |     3     |    12     |    6    |     completed      |2013-10-02|
# | 8  |     2     |    12     |    12   |     completed      |2013-10-03|
# | 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
# | 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
# +----+-----------+-----------+---------+--------------------+----------+
# The Users table holds all users. Each user has an unique Users_Id, and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).
# 
# +----------+--------+--------+
# | Users_Id | Banned |  Role  |
# +----------+--------+--------+
# |    1     |   No   | client |
# |    2     |   Yes  | client |
# |    3     |   No   | client |
# |    4     |   No   | client |
# |    10    |   No   | driver |
# |    11    |   No   | driver |
# |    12    |   No   | driver |
# |    13    |   No   | driver |
# +----------+--------+--------+
# Write a SQL query to find the cancellation rate of requests made by unbanned clients between Oct 1, 2013 and Oct 3, 2013. For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.
# 
# +------------+-------------------+
# |     Day    | Cancellation Rate |
# +------------+-------------------+
# | 2013-10-01 |       0.33        |
# | 2013-10-02 |       0.00        |
# | 2013-10-03 |       0.50        |
# +------------+-------------------+
*/


-- 2018.04.06
-- GROUP BY + SUM IF
SELECT
  Request_at AS Day,
  ROUND((SUM(IF(Status != 'completed', 1, 0)) / COUNT(*)), 2) as 'Cancellation Rate'
FROM Trips
WHERE Client_id NOT IN (SELECT Users_ID FROM Users WHERE Role = 'client' AND Banned = 'Yes')
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at


-- 2018.03.08
SELECT 
  request_at as Day,
  ROUND(SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) as 'Cancellation Rate'
FROM Trips t
JOIN Users u ON t.client_id = u.users_id
WHERE u.Banned != 'Yes' AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
ORDER BY request_at








-- 2017.04.01
select request_at as Day,
     round( ifnull((select count(*) cn1 
                    from trips t1 
                    join users u1 on u1.users_id = t1.client_id and u1.banned = 'No' 
                    where t1.request_at = t.request_at and left(status, 2) = 'ca' 
                    group by request_at), 0) / 
                    ( select count(*) cn2 
                    from trips t2 
                    join users u2 on u2.users_id = t2.client_id and u2.banned = 'No'
                    where t2.request_at = t.request_at group by request_at)
            , 2) as 'Cancellation Rate'
from trips t
where request_at between '2013-10-01' and '2013-10-03'
group by request_at
order by request_at



-- 2017.03.31
SELECT 
    t.request_at Day,
    ROUND(COUNT(IF(t.status != 'completed', TRUE, NULL))/count(*), 2) 'Cancellation Rate'
FROM Trips t
JOIN Users u
ON t.client_id = u.users_id and u.Banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'    # Watch out 10-03 not 10-3
GROUP BY t.request_at
