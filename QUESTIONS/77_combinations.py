# 77. Combinations My Submissions QuestionEditorial Solution
# Total Accepted: 76517 Total Submissions: 220533 Difficulty: Medium
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Subscribe to see which companies asked this question

# DFS. Similar to permutation
# Only differnces are:
# 1. sort nums
# 2. nums[i+1:] vs nums[:i]+nums[i+1:], in DFS call
class Solution(object):
    def dfs(self, nums, res, path, k):
        if len(path) == k:
            res.append(path)
            return
        else:
            for i in xrange(len(nums)):
                self.dfs(nums[i+1:], res, path+[nums[i]], k)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [ x for x in xrange(1, n+1)]
        self.dfs(nums, res, [], k)
        return res
             
if __name__ == "__main__":
    print(Solution().combine(20, 16))
