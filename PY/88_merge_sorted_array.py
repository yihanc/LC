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

# 2017.04.04 Shorter solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
                nums1[k] = nums1[i]
                i, k = i - 1, k - 1
            else:
                nums1[k] = nums2[j]
                j, k = j - 1, k - 1

# 2017.03.11
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        
        k = m + n - 1
        while k >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k -= 1
            
        if i == -1: 
            while k >= 0 and j >= 0:
                nums1[k] = nums2[j]
                k, j = k - 1, j - 1
        else:
            while k >= 0 and i >= 0:
                nums1[k] = nums1[i]
                k, i = k - 1, i - 1
        
        return 
        

# 11.29.2016

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        
        return
