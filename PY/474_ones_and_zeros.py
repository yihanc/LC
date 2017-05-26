# 474. Ones and Zeroes Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 9561
# Total Submissions: 25107
# Difficulty: Medium
# Contributors:
# piy9
# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
# 
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.
# 
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# 
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# 
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

# Reverse DP
# dp[m][n], maximum words using m "0" and n "1"

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [ [0 for y in xrange(n+1)] for x in xrange(m+1)]
        for s in strs:
            n0, n1 = s.count("0"), s.count("1")
            for i in xrange(m, n0 - 1, -1):
                for j in xrange(n, n1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-n0][j-n1] + 1) 
        return dp[m][n]
        


# Cases
# [u'11', u'11', u'0', u'0', u'10', u'1', u'1', u'0', u'11', u'1', u'0', u'111', u'11111000', u'0', u'11', u'000', u'1', u'1', u'0', u'00', u'1', u'101', u'001', u'000', u'0', u'00', u'0011', u'0', u'10000']
# 90
#  66
