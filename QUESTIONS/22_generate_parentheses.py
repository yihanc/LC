# 22. Generate Parentheses My Submissions QuestionEditorial Solution
# Total Accepted: 90088 Total Submissions: 240551 Difficulty: Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# "((()))", "(()())", "(())()", "()(())", "()()()"
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
