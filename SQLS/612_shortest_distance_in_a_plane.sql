/*
612. Shortest Distance in a Plane
DescriptionHintsSubmissionsDiscussSolution
Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
Write a query to find the shortest distance between these points rounded to 2 decimals.
| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
| shortest |
|----------|
| 1.00     |
Note: The longest distance among all the points are less than 10000.

*/


-- 2018.04.07

SELECT
  ROUND(POW(POW((a.x - b.x), 2) + POW((a.y - b.y), 2), 0.5), 2) AS shortest
FROM point_2d a 
LEFT JOIN point_2d b ON (a.x != b.x OR a.y != b.y)
ORDER BY shortest LIMIT 1
