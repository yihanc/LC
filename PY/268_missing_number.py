# 268. Missing Number
# DescriptionHintsSubmissionsDiscussSolution
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# 
# Example 1
# 
# Input: [3,0,1]
# Output: 2
# Example 2
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
# 
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# 2018.04.07 Set method
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in xrange(0, len(nums)):
            if i not in nums:
                return i
        return len(nums)

# 2018.02.24

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            j = nums[i]
            while j < n and j != i:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i]
        for i, num in enumerate(nums):
            if num != i:
                return i
        return n        # bug
