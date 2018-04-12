/*618. Students Report By Geography
DescriptionHintsSubmissionsDiscussSolution
A U.S graduate school has students from Asia, Europe and America. The students' location information are stored in table student as below.
| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |
Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.
For the sample input, the output is:
| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |
Follow-up: If it is unknown which continent has the most students, can you write a query to generate the student report?
*/

-- 2018.04.07
/*
The idea is Generate 3 tables for each contient with rank
Then join them back using the rank

From original table ->
T1:
Jack 1
Jane 2

T2
Xi 1

T3
Pascal 1

Then After JOIN it become
1 JACK 1 XI 1 Pascal
2 Jane null, null, null, null

*/

SELECT
  a.name as America,
  b.name as Asia,
  c.name as Europe
FROM ( SELECT @arow := @arow + 1 as row, name FROM student, (SELECT @arow := 0) init WHERE continent = 'America' ORDER BY name) a
LEFT JOIN 
    ( SELECT @brow := @brow + 1 as row, name FROM student, (SELECT @brow := 0) init WHERE continent = 'Asia' ORDER BY name) b 
ON a.row = b.row
LEFT JOIN 
    ( SELECT @crow := @crow + 1 as row, name FROM student, (SELECT @crow := 0) init WHERE continent = 'Europe' ORDER BY name) c
ON a.row = c.row


-- 2018.03.08

SELECT
    sub1.Name AS America,
    sub2.Name AS Asia,
    sub3.Name AS Europe
FROM (
    SELECT
        Name,
        @r1 := @r1 + 1 AS Rank
    FROM student s, (SELECT @r1 := 0) SQLvar1
    WHERE continent = 'America'
    ORDER BY Name) sub1
LEFT JOIN (
    SELECT
        Name,
        @r2 := IFNULL(@r2, 0) + 1 AS Rank
    FROM student s, (SELECT @r2 := 0) SQLvar2
    WHERE continent = 'Asia'
    ORDER BY Name) sub2 ON sub1.rank = sub2.rank
LEFT JOIN (
    SELECT
        Name,
        @r3 := IFNULL(@r3, 0) + 1 AS Rank
    FROM student s, (SELECT @r3 := 0) SQLvar3
    WHERE continent = 'Europe'
    ORDER BY Name) sub3 ON sub1.rank = sub3.rank
