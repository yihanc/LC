/*
626. Exchange Seats
DescriptionHintsSubmissionsDiscussSolution
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat.
*/

-- 2018.03.07

SELECT
  sub.Id,
  IFNULL(s.student, sub.student) AS student
FROM (
    SELECT
      id,
      student,
      IF(id % 2 = 1, id + 1, id - 1) as eid
    FROM
      seat 
) sub
LEFT JOIN seat s 
ON sub.eid = s.id
ORDER BY sub.Id 

