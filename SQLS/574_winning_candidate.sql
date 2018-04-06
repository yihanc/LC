/* 574. Winning Candidate
DescriptionHintsSubmissionsDiscussSolution
Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.
Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+
Notes:
You may assume there is no tie, in other words there will be at most one winning candidate.
*/




-- 2018.04.06 subquery in WHERE more Concise

SELECT Name
FROM Candidate
WHERE id = (
    SELECT CandidateId as cnt
    FROM Vote v
    GROUP BY CandidateId
    ORDER BY COUNT(*) DESC LIMIT 1
)


-- Subquery in FROM

SELECT
    c.Name
FROM (
    SELECT
      CandidateId,
      COUNT(*) as cnt
    FROM Vote v
    GROUP BY CandidateId
    ORDER BY CNT DESC LIMIT 0, 1
) sub LEFT JOIN Candidate c ON sub.CandidateId = c.id

