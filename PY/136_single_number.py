# 136. Single Number  QuestionEditorial Solution  My Submissions
# Total Accepted: 161870
# Total Submissions: 311884
# Difficulty: Easy
# Given an array of integers, every element appears twice except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res = res ^ num
        
        return res
