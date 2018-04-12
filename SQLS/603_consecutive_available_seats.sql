/*
603. Consecutive Available Seats
DescriptionHintsSubmissionsDiscussSolution
Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
Your query should return the following result for the sample case above.
| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
Note:
The seat_id is an auto increment int, and free is bool ('1' means free, and '0' means occupied.).
Consecutive available seats are more than 2(inclusive) seats consecutively available.

*/

-- 2018.04.07 two self join
SELECT a.seat_id
FROM cinema a
LEFT JOIN cinema b ON a.seat_id + 1 = b.seat_id
LEFT JOIN cinema c ON a.seat_id - 1 = c.seat_id
WHERE a.free = 1 AND (a.free = b.free OR a.free = c.free)

-- 2018.04.07 one self join
SELECT DISTINCT a.seat_id
FROM cinema a
LEFT JOIN cinema b ON abs(a.seat_id - b.seat_id) = 1
WHERE a.free = True AND a.free = b.free 
ORDER BY seat_id
