# 90. Subsets II  QuestionEditorial Solution  My Submissions
# Total Accepted: 77943
# Total Submissions: 242975
# Difficulty: Medium
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# 
# Note: The solution set must not contain duplicate subsets.
# 
# For example,
# If nums = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# Key: Same as subset except When to ignore.

# 2018.03.22
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(line, nums):
            res.append(line)
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]: 
                    continue
                dfs(line + [num], nums[i+1: ])
        
        if not nums: return []
        nums.sort()
        res = []
        dfs([], nums)
        return res


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfsHelper(res, sorted(nums), [])
        print(res)
        return res
    
    def dfsHelper(self, res, nums, line):
        res.append(line)
        for i, num in enumerate(nums):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            self.dfsHelper(res, nums[i+1:], line + [num])

if __name__ == "__main__":
    sol = Solution()
    sol.subsetsWithDup([1,2,2])
