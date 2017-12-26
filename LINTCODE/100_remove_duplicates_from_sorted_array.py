# 100. Remove Duplicates from Sorted Array 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# Have you met this question in a real interview? Yes
# Example
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
# 
# 

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) <= 1: return len(nums)
        i, n = 1, len(nums)
        while i < n:
            if nums[i] == nums[i-1]:
                del nums[i]
                n -= 1
                continue
            i += 1
        return len(nums)
