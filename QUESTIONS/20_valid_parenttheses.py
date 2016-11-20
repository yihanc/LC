# 20. Valid Parentheses My Submissions QuestionEditorial Solution
# Total Accepted: 110749 Total Submissions: 373068 Difficulty: Easy
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
