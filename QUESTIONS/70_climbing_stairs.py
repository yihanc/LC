# 70. Climbing Stairs  QuestionEditorial Solution  My Submissions
# Total Accepted: 131369
# Total Submissions: 346299
# Difficulty: Easy
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        A = []
        A.append(1)
        A.append(2)
        for i in xrange(2,n):
            A.append(A[i-1] + A[i-2])
        
        return A[n-1]
        

