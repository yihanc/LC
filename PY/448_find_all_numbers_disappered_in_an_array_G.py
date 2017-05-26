# 448. Find All Numbers Disappeared in an Array   QuestionEditorial Solution  My Submissions
# Total Accepted: 114
# Total Submissions: 215
# Difficulty: Medium
# Contributors: yuhaowang001
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# Subscribe to see which companies asked this question

# 2017.05.24
# online version o(1) space
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [ i+1 for i in xrange(len(nums)) if nums[i] > 0 ]

# 2017.05.24
# Convert to a set. o(n) space. o(n) time
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        res = []
        for i in xrange(1, len(nums) + 1):
            if i not in s: res.append(i)
        return res

