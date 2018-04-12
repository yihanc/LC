-- Q1
SELECT
  h1.name, h1.grade, h2.name, h2.grade, h3.name, h3.grade
FROM Likes l1
JOIN Likes l2 ON l1.id2 = l2.id1
JOIN Highschooler h1 ON l1.id1 = h1.id
JOIN Highschooler h2 ON l1.id2 = h2.id
JOIN Highschooler h3 ON l2.id2 = h3.id
WHERE l1.id1 != l2.id2


-- Q2
SELECT
  DISTINCT h.name, h.grade
FROM Friend f
JOIN Highschooler h ON f.id1 = h.id
WHERE f.id1 NOT IN (                    -- Subquery is the one with same grade
SELECT f1.id1
FROM Friend f1
JOIN Highschooler h1 ON f1.id1 = h1.id
JOIN Highschooler h2 ON f1.id2 = h2.id
WHERE h1.grade == h2.grade
)

-- Q3
SELECT AVG(sub.cnt)
FROM 
( SELECT ID1, COUNT(*) as cnt
FROM Friend f
GROUP BY f.id1 ) sub


-- Q4
SELECT (
( SELECT COUNT(*)
FROM Friend f
JOIN Highschooler h ON f.id1 = h.id
WHERE h.name = 'Cassandra' )
+ 
( SELECT COUNT(h3.name)
FROM Friend f1
JOIN Friend f2 ON f1.id2 = f2.id1
JOIN Highschooler h1 on f1.id1 = h1.id
JOIN Highschooler h2 on f1.id2 = h2.id
JOIN Highschooler h3 on f2.id2 = h3.id
WHERE h1.name = 'Cassandra' AND h3.name != 'Cassandra' ) )


-- Q5
SELECT h.name, h.grade
FROM Friend f
JOIN Highschooler h ON f.id1 = h.id
GROUP BY f.id1
HAVING COUNT(*) = (
SELECT COUNT(*) as cnt
FROM Friend
GROUP BY id1
ORDER BY cnt DESC LIMIT 1
)





