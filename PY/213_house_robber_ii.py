# 213. House Robber II Add to List
# Description  Submission  Solutions
# Total Accepted: 49342
# Total Submissions: 148143
# Difficulty: Medium
# Contributors: Admin
# Note: This is an extension of House Robber.
# 
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# 2017.03.14 Rewrite rob range function
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.robRange(nums, 0, n - 1), self.robRange(nums, 1, n))
        
    def robRange(self, nums, l, r):
        n = r - l
        a, b = 0, 0
        for i in xrange(l, r):
            a, b = b, max(nums[i] + a, b)
        return b
        

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.helper(nums, 0, n - 2), self.helper(nums, 1, n - 1))
    
    def helper(self, nums, l, r):
        a, b = 0, 0
        for i in xrange(l, r + 1):
            if (i + l) % 2 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])
        return max(a, b)

