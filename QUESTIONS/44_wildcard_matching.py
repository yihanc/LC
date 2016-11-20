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

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen, pLen = len(s), len(p)

        if pLen - p.count("*") > sLen:
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

