# 442. Find All Duplicates in an Array
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res

