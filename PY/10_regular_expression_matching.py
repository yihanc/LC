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
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
# Subscribe to see which companies asked this question
import unittest

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Use a 2D table to keep track of. p x s
        # 1. Fill table[0][0] = True
        # 2. Fill special case when s == 0, table[i][i] = true when p[:-2] is true and p[-1] = "*"
        # 3. if p[i-1] != "*", table[i][j] = True when table[i-1][j-1] = true and current char is matching or equal to "."
        # 4. if p[i-1] == *, table[i][j] = True when table[i-2] or table[i-1][j] match. And if p[i-2] == s[j-1]  or p[j-2] == "."
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        for i in range(2, len(p)+1):
            table[i][0] = table[i-2][0] and p[i-1] == "*"

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] != "*":
                    table[i][j] = table[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
                else:
                    table[i][j] = table[i-2][j] or table[i-1][j]
                    if p[i-2] == s[j-1] or p[i-2] == ".":
                        table[i][j] |= table[i][j-1]
        return table[-1][-1]
        

class TestSolution(unittest.TestCase):
    def test_none_0(self):
        self.assertTrue(Solution().isMatch("", ""))
        self.assertTrue(Solution().isMatch("aa", "a*"))

    def test_none_1(self):
        self.assertFalse(Solution().isMatch("a", ""))

    def test_none_2(self):
        self.assertFalse(Solution().isMatch("aa", "a"))
        self.assertTrue(Solution().isMatch("aa", "aa"))
        self.assertFalse(Solution().isMatch("aaa", "aa"))

    def test_star_0(self):
        self.assertTrue(Solution().isMatch("aa", "a*"))

    def test_dotstar_0(self):
        self.assertTrue(Solution().isMatch("aa", ".*"))

    def test_multistar_0(self):
        self.assertTrue(Solution().isMatch("aab", "c*a*b*"))

if __name__ == "__main__":
    unittest.main()
