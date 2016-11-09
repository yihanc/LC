# 88. Merge Sorted Array   QuestionEditorial Solution  My Submissions
# Total Accepted: 128598
# Total Submissions: 413850
# Difficulty: Easy
# Contributors: Admin
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
# 
# Subscribe to see which companies asked this question

# Note: m and n means something different..
# See test cases:
# [1] 1,[0] 1 -> [0]
# [1] 1,[2] 1 -> [1]
# [1,3,4,5] 2,[2] 1 ->[1,2,3,5]
# [1,3,4] 4,[2] 1 -> [1,3,4]
# [1,3,4,5] 4,[2] 1 -> [1,2,3,4]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
