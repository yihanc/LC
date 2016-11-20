# 26. Remove Duplicates from Sorted Array My Submissions QuestionEditorial Solution
# Total Accepted: 133107 Total Submissions: 394783 Difficulty: Easy
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        i = 0
        while i < len(nums):
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        
        return len(nums)
