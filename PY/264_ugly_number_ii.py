# 264. Ugly Number II Add to List
# Description  Submission  Solutions
# Total Accepted: 51613
# Total Submissions: 162400
# Difficulty: Medium
# Contributors: Admin
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# 
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
# 
# Show Hint 
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ 0 for x in xrange(n) ]
        dp[0] = 1
        p2, p3, p5 = 0, 0, 0
        
        for i in xrange(1, n):
            dp[i] = min(dp[p2] * 2, min(dp[p3] * 3, dp[p5] * 5))
            if dp[i] == dp[p2] * 2: p2 += 1
            if dp[i] == dp[p3] * 3: p3 += 1
            if dp[i] == dp[p5] * 5: p5 += 1
        
        return dp[n-1]
