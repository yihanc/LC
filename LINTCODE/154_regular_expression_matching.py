class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        dp = [ [ False for j in xrange(n+1)] for i in xrange(m+1) ]
        
        dp[0][0] = True
        for j in xrange(2, n + 1):
            if p[j-1] == "*" and dp[0][j-2]:
                dp[0][j] = dp[0][j-2]
        
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                    continue
                
                if p[j-1] == "*":
                    if dp[i][j-2]:
                        dp[i][j] = True
                        continue

                    if dp[i-1][j] and (p[j-2] == "." or p[j-2] == s[i-1]):
                        dp[i][j] = True
                        continue
        for row in dp:
            print row
        return dp[-1][-1]
                        
                    
s = "aasdfasdfasdfasdfas"
p = "aasdf.*asdf.*asdf.*asdf.*s"
        
Solution().isMatch(s, p)
