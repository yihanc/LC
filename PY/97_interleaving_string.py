# 97. Interleaving String  QuestionEditorial Solution  My Submissions
# Total Accepted: 57793
# Total Submissions: 246014
# Difficulty: Hard
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# 
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
# 
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
# 
# Subscribe to see which companies asked this question

# 2018.02.24
# Use 2D DP to record state of whether s3[i+j] can match s1[i] , s2[j]
# if s3[i+j] = s1[i], and dp[i-1][j], then dp[i][j] = True
# if s3[i+j] = s2[j],  and dp[i][j-1], then dp[i][j] = True

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2): return False
        m , n = len(s1), len(s2)
        dp = [ [False for j in xrange(n+1) ] for i in xrange(m+1) ]
        dp[0][0] = True

        for i in xrange(m + 1):
            for j in xrange(n + 1):                
                if i != 0 and s3[i+j-1] == s1[i-1] and dp[i-1][j]:
                    dp[i][j] = True
                    continue
                
                if j != 0 and s3[i+j-1] == s2[j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[m][n]
                

# 12.3.2016 

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        
        dp = [[False for j in xrange(n2+1)] for i in xrange(n1+1)]
        
        dp[0][0] = True
        
        for i in xrange(n1+1):
            for j in xrange(n2+1):
                if j > 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
                
                if i > 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
        
        return dp[-1][-1]
                

# DP
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1 + n2 != n3:
            return False

        dp = [[ False for j in xrange(n2 + 1)] for i in xrange(n1 + 1)]

        dp[0][0] = True

        for j in xrange(1, n2+1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True
    
        for i in xrange(1, n1+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True

        for i in xrange(1, n1+1):
            for j in xrange(1, n2+1):
                if (( dp[i-1][j] and s1[i-1] == s3[i+j-1] ) or 
                    ( dp[i][j-1] and s2[j-1] == s3[i+j-1] )):
                    dp[i][j] = True

#        for i in xrange(len(dp)):
#            print(dp[i])
        return dp[-1][-1]


        
if __name__ == "__main__":
    Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
    s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
    s2 ="ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
    s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
    Solution().isInterleave(s1, s2, s3)
    

exit

# DP + BFS. TOOOOOO SLOW. Repetive Calculation
from collections import deque
class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        print(s1 + " " + s2 + " " + s3)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
            
        dp = [[ False for j in xrange(n2+1)] for i in xrange(n1 + 1)]
        
        print(dp)
        dp[0][0] = True
        
        d = deque()
        d.append((0,0))
        while d:
            cur = d.pop()
            i, j = cur[0], cur[1]
            print(str(i) + " " + str(j))
            
            if i < n1 and s1[i] == s3[i+j]:
                dp[i+1][j] = True
                d.appendleft((i+1, j))
                
            if j < n2 and s2[j] == s3[i+j]:
                dp[i][j+1] = True
                d.appendleft((i, j+1))
  
        print(dp)
        return dp[-1][-1]


