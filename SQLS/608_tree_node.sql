/* Given a table tree, id is identifier of the tree node and p_id is its parent node's id.

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Each node in the tree can be one of three types:
Leaf: if the node is a leaf node.
Root: if the node is the root of the tree.
Inner: If the node is neither a leaf node nor a root node.
Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:
+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
Explanation

Node '1' is root node, because its parent node is NULL and it has child node '2' and '3'.
Node '2' is inner node, because it has parent node '1' and child node '4' and '5'.
Node '3', '4' and '5' is Leaf node, because they have parent node and they don't have child node.

And here is the image of the sample tree as below:
              1
            /   \
                      2       3
                    /   \
                  4       5
Note

If there is only one node on the tree, you only need to output its root attributes.
*/

-- 2018.04.07 Case When + Self JOIN

SELECT
  a.id,
  CASE
    WHEN (a.p_id is NULL) THEN 'Root'
    WHEN (b.id is NULL) THEN 'Leaf'
    ELSE 'Inner'
  END AS Type
FROM tree a
LEFT JOIN tree b ON a.id = b.p_id
GROUP BY a.id


-- 2018.03.07

SELECT Id,
  CASE
    WHEN t.p_id is NULL THEN "Root"
    WHEN t.p_id is NOT NULL AND sub.cnt > 0 THEN "Inner"
    ELSE "Leaf"
  END AS Type  
FROM 
  tree t
LEFT JOIN (
    SELECT p_id, count(*) as cnt
    FROM tree t
    WHERE p_id IS NOT NULL
    GROUP BY p_id ) sub
ON t.id = sub.p_id

