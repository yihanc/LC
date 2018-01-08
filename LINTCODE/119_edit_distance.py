class Solution:
    """
    @param: word1: A string
    @param: word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        m, n = len(word1), len(word2)
        
        dp = [ [ 0 for j in xrange(n+1) ] for i in xrange(m+1) ]
        
        for j in xrange(1, n + 1):
            dp[0][j] = j
        
        for i in xrange(1, m + 1):
            dp[i][0] = i
        
        
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                diag = dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1] + 1
                
                dp[i][j] = min(min(dp[i-1][j] + 1, dp[i][j-1] + 1), diag)
        
        return dp[-1][-1]
            
        

