class Solution:
    """
    @param: s1: A string
    @param: s2: A string
    @param: s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        
        dp = [ [ False for j in xrange(n2 + 1)] for i in xrange(n1 + 1) ]
        
        dp[0][0] = True
        
        for j in xrange(1, n2 + 1):
            dp[0][j] = True if dp[0][j-1] and s2[j-1] == s3[j-1] else False
        
        for i in xrange(1, n1 + 1):
            dp[i][0] = True if dp[i-1][0] and s1[i-1] == s3[i-1] else False
        
        for i in xrange(1, n1 + 1):
            for j in xrange(1, n2 + 1):
                if s3[i+j-1] == s1[i-1] and dp[i-1][j]:
                    dp[i][j] = True
                    continue
                
                if s3[i+j-1] == s2[j-1] and dp[i][j-1]:
                    dp[i][j] = True
                    continue

        return dp[-1][-1]
                
            
        
