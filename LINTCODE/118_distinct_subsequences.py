
# 12/19/2017
class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        m, n = len(S), len(T)
        dp = [ [0 for j in xrange(n + 1) ] for i in xrange(m + 1) ]
        
        dp[0][0] = 1
        
        for i in xrange(1, m + 1):
            dp[i][0] = 1
        
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if S[i-1] == T[j-1] else dp[i-1][j]
        
        #for row in dp:
        #    print(row)
        
        return dp[-1][-1]
