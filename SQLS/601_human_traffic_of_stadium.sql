/*
601. Human Traffic of Stadium
DescriptionHintsSubmissionsDiscussSolution
X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, date, people

Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

For example, the table stadium:
+------+------------+-----------+
| id   | date       | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
For the sample data above, the output is:

+------+------------+-----------+
| id   | date       | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
Note:
Each day only have one row record, and the dates are increasing with id increasing.

*/

-- 2018.03.10

SELECT
  sub1.id,
  sub1.date,
  sub1.people
FROM (
    SELECT id, date, people,
      @l1 AS l1, @l2 AS l2,
      @l2 := @l1,
    @l1 := people  
    FROM stadium s,(SELECT @l1 := NULL, @l2 := NULL) SQLvars ) sub1
LEFT JOIN (
    SELECT id, date, people,
      @a1 AS a1, 
      @a2 AS a2,
      @a2 := @a1,
      @a1 := people  
    FROM stadium s,(SELECT @a1 := NULL, @a2 := NULL) SQLvars ORDER BY date DESC ) sub2
ON sub1.date = sub2.date AND sub1.id = sub2.id AND sub1.people = sub2.people
WHERE sub1.people >= 100
  AND ( (sub1.l2 IS NOT NULL AND sub1.l2 >= 100 AND sub1.l1 IS NOT NULL AND sub1.l1 >= 100)
    OR ( sub1.l1 IS NOT NULL AND sub1.l1 >= 100 AND sub2.a1 IS NOT NULL AND sub2.a1 >= 100)
    OR ( sub2.a1 IS NOT NULL AND sub2.a1 >= 100 AND sub2.a2 IS NOT NULL AND sub2.a2 >= 100) )
ORDER BY sub1.id
