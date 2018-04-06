/*571. Find Median Given Frequency of Numbers
DescriptionHintsSubmissionsDiscussSolution
The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.
*/


-- 2018.04.06
SELECT AVG(Number) as median
From Numbers n
WHERE n.Frequency >=
ABS((SELECT SUM(FREQUENCY) FROM Numbers n1 WHERE n.Number >= n1.Number) -
(SELECT SUM(FREQUENCY) FROM Numbers n2 WHERE n.Number <= n2.Number))


-- 2018.03.08

SELECT ROUND(MAX(sub.median), 4) AS median
FROM (
SELECT
  @cur := @cur + Frequency,
  Number,
  Frequency,
  @n1 := IF(@cur >= (@total DIV 2) AND @n1 IS NULL, Number, @n1) as n1, 
  @n2 := IF(@cur >= (@total DIV 2) + 1 AND @n2 IS NULL, Number, @n2) as n2,
  IF(@n2 IS NULL, NULL, IF(@total % 2 = 1.0, @n2, (@n1 + @n2) / 2)) AS median
FROM Numbers n,
    (
    SELECT 
        @cur := 0,
        @n1 := NULL, 
        @n2 := NULL, 
        @total := (SELECT SUM(Frequency) FROM Numbers)) SQLvars
ORDER BY Number
) sub
