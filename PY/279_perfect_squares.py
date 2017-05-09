# 279. Perfect Squares Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 71739
# Total Submissions: 199225
# Difficulty: Medium
# Contributor: LeetCode
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
# 
# 

# 2017.05.07 DP
# 72xx ms
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        while len(dp) <= n:
            cmin = n + 1
            for i in xrange(1, int(len(dp) ** 0.5) + 1):
                cmin = min(cmin, dp[len(dp) - i * i])
            dp.append(cmin + 1)
        return dp[n]


# 2017.05.06 too slow
# DP
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ n << 1 for x in xrange(n + 1) ]
        dp[0] = 0
        for i in xrange(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]
