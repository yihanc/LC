# 564. Backpack VI 
# Given an integer array nums with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# 
#  Notice
# A number in the array can be used multiple times in the combination. 
# Different orders are counted as different combinations.
# 
# Have you met this question in a real interview? Yes
# Example
# Given nums = [1, 2, 4], target = 4
# 
# The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]
# return 6

# 12.30.2017
# Scan from 1 to target
class Solution:
    """
    @param: nums: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        dp = [ 0 for x in xrange(target + 1) ]
        
        dp[0] = 1
        
        for i in xrange(1, target + 1):
            for j in xrange(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
            
