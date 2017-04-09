/*
# 178. Rank Scores Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 18738 Total Submissions: 79655 Difficulty: Medium
# Contributor: LeetCode
# Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
# 
# +----+-------+
# | Id | Score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+
# For example, given the above Scores table, your query should generate the following report (order by highest score):
# 
# +-------+------+
# | Score | Rank |
# +-------+------+
# | 4.00  | 1    |
# | 4.00  | 1    |
# | 3.85  | 2    |
# | 3.65  | 3    |
# | 3.65  | 3    |
# | 3.50  | 4    |
# +-------+------+
# Subscribe to see which companies asked this question.
*/








-- Another good short solution
SELECT
  Score,
  (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) tmp WHERE s >= Score) Rank
FROM Scores
ORDER BY Score desc


-- Another simple solution. But got TLE for large case
select Score, (1+ (Select count(distinct B.Score) from Scores as B where B.score > A.score)) as Rank
from Scores as A
order by Rank;


select s.Score, tmp.rank as Rank
from Scores s
left join ( select t.score, @rownum := @rownum + 1 as rank
            from (select distinct score from scores order by score desc) t
            join (select @rownum := 0) r 
          ) tmp on s.score = tmp.score
order by s.score desc
