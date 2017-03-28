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

# 2017.03.24 DFS inside
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(line, A, tgt):
            if tgt < 0: return
            if tgt == 0:
                res.append(line)
                return
            
            for i in xrange(len(A)):
                if i == 0 or A[i] != A[i-1]:
                    dfs(line + [A[i]], A[i+1:], tgt - A[i])
        
        candidates.sort()
        res = []
        dfs([], candidates, target)
        return res

# 12.17.2016 Rewrite. Faster
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(res, [], candidates, target)
        return res
    
    def dfs(self, res, line, candidates, target):
        if sum(line) == target:
            res.append(line)
            return
        
        for i in xrange(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            
            if sum(line) + candidates[i] <= target:
                self.dfs(res, line + [candidates[i]], candidates[i+1:], target)
            else:
                break

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

        if sumList > target:
            return

        for i, num in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                self.dfsHelper(res, nums[i+1:], line + [num], target)
