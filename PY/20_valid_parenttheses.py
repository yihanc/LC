# 20. Valid Parentheses My Submissions QuestionEditorial Solution
# Total Accepted: 110749 Total Submissions: 373068 Difficulty: Easy
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# 
# Subscribe to see which companies asked this question

from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {")" : "(", "]": "[", "}": "{" }
        d = deque()
        
        for char in s:
            # Peek right most
            if d:
                cur = d.pop() 
                d.append(cur)
            else:
                cur = None

            if char in "([{":
                d.append(char)
            elif char in ")]}" and dic[char] != cur:
                return False
            elif char in ")]}":
                d.pop()

        return True if not d else False

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)

    def test_1(self):
        self.assertEqual(Solution().isValid("([)]"), False)

if __name__ == "__main__":
    unittest.main()
