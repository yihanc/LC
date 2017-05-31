# 303. Range Sum Query - Immutable
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 66614
# Total Submissions: 234629
# Difficulty: Easy
# Contributor: LeetCode
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# 
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

# 2017.05.30 
# if no update, prefix array is perfect
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0 for x in xrange(len(nums) + 1)]
        for i in xrange(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix[j+1] - self.prefix[i]
