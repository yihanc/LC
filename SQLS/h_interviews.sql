/* Interviews 
by AvimanyuSingh
Problem
Submissions
Leaderboard
Discussions
Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are .

Note: A specific contest can be used to screen candidates at more than one college, but each college only holds screening contest.

Input Format

The following tables hold interview data:

Contests: The contest_id is the id of the contest, hacker_id is the id of the hacker who created the contest, and name is the name of the hacker. 

Colleges: The college_id is the id of the college, and contest_id is the id of the contest that Samantha used to screen the candidates. 

Challenges: The challenge_id is the id of the challenge that belongs to one of the contests whose contest_id Samantha forgot, and college_id is the id of the college where the challenge was given to candidates. 

View_Stats: The challenge_id is the id of the challenge, total_views is the number of times the challenge was viewed by candidates, and total_unique_views is the number of times the challenge was viewed by unique candidates. 

Submission_Stats: The challenge_id is the id of the challenge, total_submissions is the number of submissions for the challenge, and total_accepted_submission is the number of submissions that achieved full scores. 

Sample Input

Contests Table: Colleges Table: Challenges Table: View_Stats Table: Submission_Stats Table: 

Sample Output

66406 17973 Rose 111 39 156 56
66556 79153 Angela 0 0 11 10
94828 80275 Frank 150 38 41 15
Explanation

The contest  is used in the college . In this college , challenges  and  are asked, so from the view and submission stats:

Sum of total submissions 

Sum of total accepted submissions 

Sum of total views 

Sum of total unique views 

Simillarly, we can find the sums for contests  and .1
*/



select ct.contest_id, ct.hacker_id, ct.name, 
    sum(tmp2.ts) s1, sum(tmp2.tas) s2,
    sum(tmp1.tv) s3, sum(tmp1.tuv) s4
from contests ct
join colleges cl on cl.contest_id = ct.contest_id
join challenges ch on ch.college_id = cl.college_id
left join (select challenge_id, sum(total_views) tv, sum(total_unique_views) tuv from view_stats group by challenge_id)            tmp1 on tmp1.challenge_id = ch.challenge_id
left join (select challenge_id, sum(total_submissions) ts, sum(total_accepted_submissions) tas from submission_stats              group by challenge_id) tmp2 on tmp2.challenge_id = ch.challenge_id
group by ct.contest_id
having s1 > 0 or s2 > 0 or s3 > 0 or s4 > 0
order by ct.contest_id
