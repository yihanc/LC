# 44. Wildcard Matching My Submissions QuestionEditorial Solution
# Total Accepted: 59032 Total Submissions: 333961 Difficulty: Hard
# Implement wildcard pattern matching with support for '?' and '*'.
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# The matching should cover the entire input string (not partial).
# 
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# 
# Some examples:
# isMatch("aa","a")  false
# isMatch("aa","aa")  true
# isMatch("aaa","aa")  false
# isMatch("aa", "*")  true
# isMatch("aa", "a*")  true
# isMatch("ab", "?*")  true
# isMatch("aab", "c*a*b")  false

# 2018.02.22
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [ [False for j in xrange(n + 1)] for i in xrange(m + 1) ] 
        dp[0][0] = True
        
        for j in xrange(1, n+1):
            if p[j-1] == "*" and dp[0][j-1] is True:
                dp[0][j] = True
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if (s[i-1] == p[j-1] or p[j-1] == "?") and dp[i-1][j-1] is True:
                    dp[i][j] = True
                    continue
                
                if p[j-1] == "*":
                    if dp[i][j-1] is True or dp[i-1][j] is True:
                        dp[i][j] = True
        
        return dp[m][n]
        

# 11.19.2016 Same template
# 1. Initialize dp
# 2. Handle non "*" case
# 3. Handle "*" case. Matching 0. Matching 1
# 
# Only differences with Regular Expression
# 1. Deal with extra large case
# Matching 0 "*", dp[i][j-1]
# Matching 1 "*", dp[i-1][j]
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        if n - p.count("*") > m: return False
        
        dp = [[False for y in xrange(n+1)] for x in xrange(m+1)]
        
        dp[0][0] = True
        
        for j in xrange(1, n+1):
            if p[j-1] == "*" and dp[0][j-1]:
                dp[0][j] = True
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if (p[j-1] == "?" or p[j-1] == s[i-1]) and dp[i-1][j-1]:
                    dp[i][j] = True
                    continue
            
                if p[j-1] == "*":
                    if dp[i][j-1] or dp[i-1][j]:
                        dp[i][j] = True

        
        return dp[-1][-1]

class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen, pLen = len(s), len(p)

        if pLen - p.count("*") > sLen:  # Corner Case:
            return False

        dp = [[ False for j in xrange(pLen+1)] for i in xrange(sLen+1)]

        dp[0][0] = True

        for j in xrange(1, pLen+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]

        for i in xrange(1, sLen+1):
            for j in xrange(1, pLen+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]
                







class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True

        if pLen - p.count('*') > sLen:   #avoid TLE
            return False

        i, j = 0, 0
        while i < len(s) and j < len(p):
            print(str(i) + " " + str(j))
            if s[i] != p[j]:
                return False
                
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
                continue
        
            while p[j] == '*':
                j += 1
    
            if j == len(p):
                return True
        
        if i == len(s) and j == len(p):
            return True
        else:
            return False


# Python TLE. Too slow
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen, pLen = len(s), len(p)
        dp = [[False for i in xrange(0, pLen+1)] for j in xrange(0, sLen+1)]
        dp[0][0] = True
        print(dp)
        
        for j in xrange(0, pLen):
            print("-- j: " + str(j))
            if p[j] == '*':
                dp[0][j+1] = dp[0][j];
            print(dp)
        
        for i in xrange(0, sLen):
            for j in xrange(0, pLen):
                print("-- i: " + str(i) + " --- j: " + str(j))
                if s[i] == p[j] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                print(dp)
        
        return dp[sLen][pLen]

if __name__ == "__main__":
#    print(Solution().isMatch("aa", "a"))
#    print(Solution().isMatch("aaa", "*b"))
    print(Solution().isMatch("aaa", "*b"))

