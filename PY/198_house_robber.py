# 198. House Robber Add to List
# Description  Submission  Solutions
# Total Accepted: 118530
# Total Submissions: 313969
# Difficulty: Easy
# Contributors: Admin
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
# 
# Subscribe to see which companies asked this question.

# Rewrite shorter version
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a, b = 0, 0
        for i in xrange(n):
            a, b = b, max(nums[i] + a, b) 
        return b

# DP 2017.03.04
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        a, b = nums[0], max(nums[0], nums[1])
        
        for i in xrange(2, n):
            a, b = b, max(a + nums[i], b)
        
        return b

# DP 2017.02.25
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [ 0 for x in xrange(n) ]
        if n > 0: dp[0] = nums[0]
        if n > 1: dp[1] = max(nums[1], nums[0])
        
        for i in xrange(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
            
# Non-dp solution
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in xrange(len(nums)):
            if i % 2 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])
        return max(a, b)
        
