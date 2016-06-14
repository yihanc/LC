# 39. Combination Sum My Submissions QuestionEditorial Solution
# Total Accepted: 93827 Total Submissions: 299696 Difficulty: Medium
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2,  , ak) must be in non-descending order. (ie, a1  a2    ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3] 
# Subscribe to see which companies asked this question

# DFS
# Similar to combination
# Passing nums[i:] to DFS call
class Solution(object):
    def dfs(self, nums, res, path, sum, target):
        if sum == target:
            res.append(path)
        elif sum > target:
            return
        else:
            for i, num in enumerate(nums):
                self.dfs(nums[i:], res, path+[num], sum+num, target)
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, res, [], 0, target)
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        A = Solution().combinationSum([2,3,4,7], 7)
        B = [[2,2,3], [3,4], [7]]
        self.assertEqual(A, B)

if __name__ == "__main__":
    unittest.main()
