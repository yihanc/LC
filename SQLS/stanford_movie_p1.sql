/*
Movie ( mID, title, year, director ) 
English: There is a movie with ID number mID, a title, a release year, and a director. 

Reviewer ( rID, name ) 
English: The reviewer with ID number rID has a certain name. 

Rating ( rID, mID, stars, ratingDate ) 
English: The reviewer rID gave the movie mID a number of stars rating (1-5) on a certain ratingDate. 

Your queries will run over a small data set conforming to the schema. View the database. (You can also download the schema and data.) 
*/

-- Q1

SELECT title FROM Movie WHERE director = 'Steven Spielberg';


-- Q2
SELECT DISTINCT year
FROM Movie m
LEFT JOIN Rating r ON m.mID = r.mId
WHERE stars = 4 OR stars = 5
ORDER BY year


-- Q3
SELECT title
FROM Movie m
WHERE m.mID not IN (
SELECT DISTINCT Mid FROM Rating
)


-- Q4

SELECT a.name
FROM Reviewer a
JOIN Rating b ON a.rId = b.rid
WHERE ratingDate is NULL

-- Q5

SELECT
  re.name,
  m.title,
  ra.stars,
  ra.ratingDate
FROM Rating ra
LEFT JOIN Movie m ON ra.mid = m.mid
LEFT JOIN Reviewer re ON ra.rid = re.rid
ORDER BY re.name, m.title, ra.stars


-- Q6

SELECT
  re.name,
  m.title
FROM rating a
JOIN rating b ON a.rid = b.rid 
AND a.mid = b.mid AND a.ratingDate > b.ratingDate AND a.stars > b.stars
LEFT JOIN Movie m ON a.mid = m.mid
LEFT JOIN Reviewer re on a.rid = re.rid


-- Q7
SELECT
  m.title,
  MAX(stars)
FROM Rating r
LEFT JOIN Movie m ON r.mid = m.mid
GROUP BY r.mid
ORDER BY m.title


-- Q8

SELECT
  m.title,
  MAX(stars) - MIN(stars)
FROM Rating r
LEFT JOIN Movie m ON r.mid = m.mid
GROUP BY r.mid
ORDER BY DIFF DESC, m.title

-- Q9


SELECT AVG(before.avg) - AVG(after.avg)
FROM ( 
SELECT AVG(stars) as avg
FROM Rating
WHERE mid IN ( SELECT mid FROM Movie WHERE year < 1980)
GROUP BY mid ) before, 
( 
SELECT AVG(stars) as avg
FROM Rating
WHERE mid IN ( SELECT mid FROM Movie WHERE year >= 1980)
GROUP BY mid 
) after
