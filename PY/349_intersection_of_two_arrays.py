# 349. Intersection of Two Arrays   QuestionEditorial Solution  My Submissions
# Total Accepted: 58267
# Total Submissions: 129340
# Difficulty: Easy
# Contributors: Admin
# Given two arrays, write a function to compute their intersection.
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# Note:
# Each element in the result must be unique.
# The result can be in any order.
# Subscribe to see which companies asked this question

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        for num in nums1:
            if num not in dic:
                dic[num] = True
        
        for num in nums2:
            if num in dic:
                res.append(num)
                del dic[num]
        
        return res
