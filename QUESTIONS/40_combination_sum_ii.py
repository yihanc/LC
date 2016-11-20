# 40. Combination Sum II My Submissions QuestionEditorial Solution
# Total Accepted: 70928 Total Submissions: 253965 Difficulty: Medium
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfsHelper(res, sorted(candidates), [], target)
        return res

    def dfsHelper(self, res, nums, line, target):
        sumList = sum(line)
        if sumList == target:
            res.append(line)
            return
        elif sumList > target:
            return
        else:
            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.dfsHelper(res, nums[i+1:], line + [num], target)
