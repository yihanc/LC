# 115. Distinct Subsequences  QuestionEditorial Solution  My Submissions
# Total Accepted: 58829
# Total Submissions: 195644
# Difficulty: Hard
# Given a string S and a string T, count the number of distinct subsequences of T in S.
# 
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# 
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# Return 3.
# 
# Subscribe to see which companies asked this question

# 1.1.2017 Rewrite
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [ [ 0 for y in xrange(n+1) ] for x in xrange(m+1) ]
        
        dp[0][0] = 1
        
        for i in xrange(1, m+1):
            for j in xrange(min(i+1, n+1)):   # dp = 0 if len(s) < len(t)
                if j == 0:
                    dp[i][0] = 1
                    continue
                
                dp[i][j] = dp[i-1][j]           # always = dp[i-1][j-1]
                
                if s[i-1] == t[j-1]:            # if matched, +dp[i-1][j-1]
                    dp[i][j] += dp[i-1][j-1] 
        
        return dp[-1][-1]
                

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        
        for i in xrange(m+1):
            dp[i][0] = 1
        
        for j in xrange(1, n+1):
            dp[0][j] = 0
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if s[i-1] == t[j-1]:        # If equal. Add dp[i-1][j-1]
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:                       # If not, just dp[i-1][j]
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        
if __name__ == "__main__":
    Solution().numDistinct("a", "b")
