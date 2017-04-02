/*
Contest Leaderboard 
by AvimanyuSingh
Problem
Submissions
Leaderboard
Discussions
You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

Input Format

The following tables contain contest data:

Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 

Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission. 

Sample Input

Hackers Table: 

Submissions Table: 

Sample Output

4071 Rose 191
74842 Lisa 174
84072 Bonnie 100
4806 Angela 89
26071 Frank 85
80305 Kimberly 67
49438 Patrick 43
Explanation

Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score .

Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score 

Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score .

The total scors for hackers 4806, 26071, 80305, and 49438 can be similarly calculated. */








select
    tmp.hacker_id, h.name, sum(tmp.mx) tot
from 
    ( select s.hacker_id, max(s.score) mx, challenge_id
    from submissions s
    group by hacker_id, challenge_id
    having mx > 0) tmp
join hackers h on h.hacker_id = tmp.hacker_id
group by tmp.hacker_id
order by tot desc, tmp.hacker_id 

