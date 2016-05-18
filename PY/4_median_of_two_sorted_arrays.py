# 4. Median of Two Sorted Arrays   My Submissions QuestionEditorial Solution
# Total Accepted: 94496 Total Submissions: 504037 Difficulty: Hard
# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        
        if m == 0 or n == 0:
            raise ValueError
        
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i > 0 and j < n and nums1[i-1] > nums2[j]:
                # i too big
                imax = i - 1
            elif j > 0 and i < m and nums2[j-1] > nums1[i]:
                # j too big, i too small
                imin = i + 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if m + n % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right ) / 2.0
