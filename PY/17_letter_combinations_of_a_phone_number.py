# 17. Letter Combinations of a Phone Number My Submissions QuestionEditorial Solution
# Total Accepted: 81591 Total Submissions: 280756 Difficulty: Medium
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# 

from collections import deque

# Iterative Loop
class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        
        dic = { "1": "",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
                "0": " " }
        
        res = []
        
        for digit in digits:
            line = ""
            for line in res:
                print("--------" + line)
                for char in dic[digit]:
                    print("---" + char)
                    res.append(line + char)
        
        return res

# DFS and FIFO
class Solution(object):
    def dfs(self, d, res, line):
        if not d:
            res.append(line)
        else:
            cur = d.pop()
            for char in cur:
                self.dfs(d, res, line + char)
            d.append(cur)
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = { "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " " }
        d = deque()
        res, line = [], ""
        
        for digit in digits:
            d.appendleft(dic[digit])
        
        self.dfs(d, res, line)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(Solution2().letterCombinations("23")), expected)

    def test_1(self):
        expected = ["a", "b", "c"]
        self.assertEqual(sorted(Solution2().letterCombinations("2")), expected)

if __name__ == "__main__":
    unittest.main()
