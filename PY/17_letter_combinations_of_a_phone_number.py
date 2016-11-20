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

# Non DFS. 11.19.2016
from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        dic = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        for digit in digits:
            tmp = res
            res = []            
            for char in dic[str(digit)]:
                if len(tmp) == 0:
                    res.append(char)
                
                for i in xrange(len(tmp)):
                    res.append(tmp[i] + char)
        
        return res


# DFS only
class Solution(object):
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

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        res = []
        self.dfs(digits, 0, res, "")
        return res

    def dfs(self, digits, i, res, line):
        if i == len(digits):
            res.append(line)
            return

        for char in self.dic[digits[i]]:
            self.dfs(digits, i+1, res, line + char)

#####

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
