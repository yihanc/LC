# 377. Combination Sum IV Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 30365
# Total Submissions: 72851
# Difficulty: Medium
# Contributors: Admin
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

# 2018.03.22 DP
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [ 0 for i in xrange(target + 1)]
        dp[0] = 1
        
        for i in xrange(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]



# DP Much faster.. For calculating
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [ 0 for _ in xrange(target + 1)]
        dp[0] = 1
        
        for i in xrange(1, target + 1):
            for j in xrange(n):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
        
        return dp[-1]

## DFS too slow
# Case [4,2,1], 32 failed
#
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0]
        self.dfs(res, nums, target)
        return res[0]
    
    def dfs(self, res, nums, target):
        #print(line, nums, target)
        if target < 0:
            return
        
        if target == 0:
            res[0] += 1
            return
        
        for i in xrange(len(nums)):
            self.dfs(res, nums, target - nums[i])
