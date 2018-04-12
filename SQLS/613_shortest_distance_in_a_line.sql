/*613. Shortest Distance in a Line
DescriptionHintsSubmissionsDiscussSolution
Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.
Write a query to find the shortest distance between two points in these points.
| x   |
|-----|
| -1  |
| 0   |
| 2   |
The shortest distance is '1' obviously, which is from point '-1' to '0'. So the output is as below:
| shortest|
|---------|
| 1       |
Note: Every point is unique, which means there is no duplicates in table point.
Follow-up: What if all these points have an id and are arranged from the left most to the right most of x axis?
*/

-- 2018.03.10 Self join

SELECT
  b.x - a.x as shortest
FROM point a
JOIN point b ON a.x < b.x
ORDER BY shortest LIMIT 1

-- 

SELECT 
  min(sub.x - sub.last) AS shortest
FROM (
    SELECT
      x,
      @last AS last,
      @last := x
    FROM point, (SELECT @last := NULL) SQLvars
) sub
WHERE sub.last IS NOT NULL

