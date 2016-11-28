# 32. Longest Valid Parentheses My Submissions QuestionEditorial Solution
# Total Accepted: 64017 Total Submissions: 283620 Difficulty: Hard
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# 
# Subscribe to see which companies asked this question

# 
#  Using a Queue to store index that are not matched
# Scan queue to get all substring and update max length

# 11.22.2016 Rewrite
# Idea: Use a deque to record index which are not matched
# Traverse dequeu to get max length of each seg.
from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, d = 0, deque()
        
        for i in xrange(len(s)):
            if d and s[i] == ")" and s[d[-1]] == "(":
                d.pop()
            else:
                d.append(i)

        d.append(len(s))
        start = -1
        for index in d:
            res = max(res, index - start - 1)
            start = index
            
        return res

from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        d = deque()
        
        # 1. Scan to 
        i = 0
        while i < len(s):
            if d: 
                peek = d.pop()
                d.append(peek)
            if d and s[peek] == "(" and s[i] == ")":
                d.pop()
            else:
                d.append(i)
            i += 1

        # 2 Scan again to update max
        start = res = 0
        while d:
            end = d.popleft()
            res = max(res, end - start)
            start = end + 1

        res = max(res, len(s) - start)
        return res
        
import unittest
class TestSolution(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(Solution().longestValidParentheses(")"), 0)
        self.assertEqual(Solution().longestValidParentheses("("), 0)
        self.assertEqual(Solution().longestValidParentheses(""), 0)
        self.assertEqual(Solution().longestValidParentheses("))"), 0)
        self.assertEqual(Solution().longestValidParentheses("))("), 0)
        self.assertEqual(Solution().longestValidParentheses("))(("), 0)
        self.assertEqual(Solution().longestValidParentheses(")))((("), 0)

    def test_case_1(self):
        self.assertEqual(Solution().longestValidParentheses("(()"), 2)
        self.assertEqual(Solution().longestValidParentheses("((()"), 2)
        self.assertEqual(Solution().longestValidParentheses("()))"), 2)

    def test_case_2(self):
        self.assertEqual(Solution().longestValidParentheses("()(()"), 2)

if __name__ == "__main__":
    unittest.main()
