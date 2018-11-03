# 674. Longest Continuous Increasing Subsequence
# DescriptionHintsSubmissionsDiscussSolution
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

# 2018.11.2
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cur = 1
        res = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res
