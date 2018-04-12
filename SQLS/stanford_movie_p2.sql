-- Q1
SELECT DISTINCT re.name
FROM Reviewer re
JOIN Rating ra ON re.rid = ra.rid
JOIN Movie m ON ra.mid = m.mid
WHERE m.title = 'Gone with the Wind'


-- Q2
SELECT
  re.name,
  m.title,
  ra.stars
FROM Rating ra
JOIN Movie m ON ra.mid = m.mid
JOIN Reviewer re ON ra.rid = re.rid
WHERE m.director = re.name



