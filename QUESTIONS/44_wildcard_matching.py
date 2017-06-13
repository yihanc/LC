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
        print(s, p)
        m, n = len(s), len(p)
        dp = [ [ False for y in xrange(n + 1) ] for x in xrange(m + 1) ]
        dp[0][0] = True

        for j in xrange(1, n + 1):
            if p[j-1] == "*" and dp[0][j-1]:
                dp[0][j] = True

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if (s[i-1] == p[j-1] or p[j-1] == "?") and dp[i-1][j-1]:    #Cur char matching
                    dp[i][j] = True

                if p[j-1] == "*":
                    if dp[i][j-1] or dp[i-1][j]:    # Matching 0 or more
                        dp[i][j] = True          

        for row in dp:
            print(row)
        return dp[-1][-1]
            

if __name__ == "__main__":
    print(Solution().isMatch("aa","a"))
    print(Solution().isMatch("aa","aa"))
    print(Solution().isMatch("aaa","aa"))
    print(Solution().isMatch("aa", "*"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("ab", "?*"))
    print(Solution().isMatch("aab", "c*a*b"))
