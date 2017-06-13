# 10. Regular Expression Matching My Submissions QuestionEditorial Solution
# Total Accepted: 81042 Total Submissions: 366383 Difficulty: Hard
# Implement regular expression matching with support for '.' and '*'.
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*")  true
# isMatch("aa", ".*")  true
# isMatch("ab", ".*")  true
# isMatch("aab", "c*a*b")  true
# Subscribe to see which companies asked this question
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "aa"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("ab", ".*"))
    print(Solution().isMatch("aab", "c*a*b"))

