# 22. Generate Parentheses My Submissions QuestionEditorial Solution
# Total Accepted: 90088 Total Submissions: 240551 Difficulty: Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# "((()))", "(()())", "(())()", "()(())", "()()()"
# 
# Subscribe to see which companies asked this question

# 11.19.2016. Rewrite DFS. Clear
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, "", n, 0)
        return res
        
    def dfs(self, res, line, lefts, rights):
        if lefts == 0 and rights == 0:
            res.append(line)
            return
        
        if lefts > 0:
            self.dfs(res, line + "(", lefts - 1, rights + 1)
        
        if rights > 0:
            self.dfs(res, line + ")", lefts, rights - 1)

        

# DFS, l r to keep track of
class Solution2(object):
    def dfs(self, l, r,  n, line, res):
        # l, r for the number of (, ) in line
        if l == n and r == n:
            res.append(line)
            return
        elif l > n or r > n:
            return
        else:
            for char in "()":
                # Case "("
                if char == "(":
                    self.dfs(l+1, r, n, line+char, res)
                # Case ")"
                elif l > r and char == ")":
                    self.dfs(l, r+1, n, line+char, res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(0, 0, n, "", res)
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().generateParenthesis(0), [""]) 

    def test_1(self):
        self.assertEqual(Solution().generateParenthesis(1), ["()"])

    def test_2(self):
        self.assertEqual(Solution().generateParenthesis(2), ["(())", "()()"])

    def test_3(self):
        self.assertEqual(Solution().generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

if __name__ == "__main__":
    unittest.main()
