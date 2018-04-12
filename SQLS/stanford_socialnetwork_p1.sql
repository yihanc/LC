-- Q1
SELECT DISTINCT h2.name
FROM ( 
SELECT ID1 as first, ID2 as second
FROM friend
UNION ALL
SELECT ID2 as first, ID1 as second
FROM friend ) sub
LEFT JOIN Highschooler h1 ON sub.first = h1.id
LEFT JOIN Highschooler h2 ON sub.second = h2.id
WHERE h1.name = 'Gabriel'


-- Q2
SELECT
  h1.name, h1.grade, h2.name, h2.grade
FROM ( 
SELECT ID1 as first, ID2 as second
FROM Likes
UNION ALL
SELECT ID2 as first, ID1 as second
FROM Likes ) j
LEFT JOIN Highschooler h1 ON j.first = h1.id
LEFT JOIN Highschooler h2 ON j.second = h2.id
WHERE h1.grade - h2.grade >= 2


-- Q3
SELECT h1.name, h1.grade, h2.name, h2.grade
FROM ( 
SELECT ID1 as first, ID2 as second
FROM Likes
UNION ALL
SELECT ID2 as first, ID1 as second
FROM Likes ) j
LEFT JOIN Highschooler h1 ON j.first = h1.id
LEFT JOIN Highschooler h2 ON j.second = h2.id
WHERE h1.name < h2.name
GROUP BY j.first, j.second
HAVING COUNT(*) > 1


-- Q4
SELECT h.name, h.grade
FROM Highschooler h
WHERE ID NOT IN (SELECT ID1 FROM LIKES UNION SELECT ID2 FROM LIKES)
ORDER BY h.grade, h.name


-- Q5
SELECT
  h1.name, h1.grade, h2.name, h2.grade
FROM Likes l
JOIN Highschooler h1 ON l.id1 = h1.id
JOIN Highschooler h2 ON l.id2 = h2.id
WHERE id2 NOT IN (
SELECT DISTINCT id1 FROM Likes
) 


-- Q6 tricky
SELECT
  name, grade
FROM Highschooler h
LEFT JOIN (
SELECT
  f.id1, f.id2
FROM Friend f
JOIN Highschooler h1 ON f.ID1 = h1.id
JOIN Highschooler h2 ON f.ID2 = h2.id
WHERE h1.grade != h2.grade ) sub ON h.id = sub.id1 OR h.id = sub.id2
WHERE sub.id1 IS NULL or sub.id2 IS NULL
ORDER BY grade, name


-- Q7 hard
-- For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). For all such trios, return the name and grade of A, B, and C. 

SELECT
  h1.name, h1.grade, h2.name, h2.grade, h3.name, h3.grade   -- h1 A, h2 B, h3 C (common friend)
FROM Likes l
JOIN Friend f1 ON l.id1 = f1.id1       -- f1.id2 is A's friends
JOIN Friend f2 ON f1.id2 = f2.id1       -- f2.id1 is A's friends friends
JOIN Highschooler h1 ON l.id1 = h1.id
JOIN Highschooler h2 ON l.id2 = h2.id
JOIN Highschooler h3 ON f1.id2 = h3.id
WHERE (Select COUNT(*) FROM Friend f WHERE l.id1 = f.id1 AND l.id2 = f.id2) = 0     -- A,B not friends
AND l.id2 = f2.id2      -- Check A's friends friends have B


-- Q8
SELECT COUNT(ID) - COUNT(DISTINCT name)
FROM Highschooler  


-- Q9
SELECT h.name, h.grade
FROM Likes l
JOIN Highschooler h ON l.id2 = h.id
GROUP BY id2
HAVING COUNT(*) > 1




