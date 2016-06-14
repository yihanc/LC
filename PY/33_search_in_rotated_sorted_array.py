# 33. Search in Rotated Sorted Array My Submissions QuestionEditorial Solution
# Total Accepted: 104226 Total Submissions: 341737 Difficulty: Hard
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            # Special cases
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            # Cases to update left or right (Note: mid == l)
            # 1. l < target < mid
            # 2. l < target, l > mid
            # 3. target < mid, mid < l
            if ((target < nums[mid] and target > nums[l] ) or
                (nums[l] > nums[mid] and (nums[l] < target or target < nums[mid]))):
                r = mid - 1
            else:
                l = mid + 1
        
        if target == nums[l]: return l
        else: return -1
