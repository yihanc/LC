# 132. Palindrome Partitioning II  QuestionEditorial Solution  My Submissions
# Total Accepted: 58982
# Total Submissions: 256833
# Difficulty: Hard
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [ n for x in xrange(n+1)]
        dp[0] = -1

        for i in xrange(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j] + 1)
                j += 1

            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i-j+1] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j+1] + 1)
                j += 1

        return dp[-1]
