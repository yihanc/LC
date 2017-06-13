# 4. Median of Two Sorted Arrays   My Submissions QuestionEditorial Solution
# Total Accepted: 94496 Total Submissions: 504037 Difficulty: Hard
# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 

# 2017.04.4 Another solution. Maintaining a res[2]
# Time complexity O((m + n) // 2)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m == 0 and n == 0: return 0
        if m + n == 1: return nums1[1] if m == 1 else nums2[1]
        i, j, k = 0, 0, 0
        res = [None, None]
        while i < m or j < n:
            if j == n or (i < m and nums1[i] < nums2[j]):
                res = [res[1], nums1[i]]
                i += 1
            else:
                res = [res[1], nums2[j]]
                j += 1
            k += 1
            if k - 1 == (m + n + 1) // 2: break
        return res[0] if (m + n) & 1 else sum(res) / 2.0


# 2017.06.01 Rewrite
# Standard best solution but hard to implement and understand. O(min(
# Time complexity O(log(min(m, n)))
# Find i, so that nums1[: i] + nums2[:j] = nums1[i:] , nums2[j:]
# 0 1 2 3 4 5  6 7
# m + n = 8, i + j = 4, i = 0 j = 4 return max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])
# 0 1 2 3 4 5 6
# m + n = 7, i + j = 4, i = 0, j = 4, return max(nums1[i-1], nums2[j-1])

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax ) // 2
            j = half_len - i
            
            if j > 0 and i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                break
        
        if i == 0: left_max = nums2[j-1]
        elif j == 0: left_max = nums1[i-1]
        else: left_max = max(nums1[i-1], nums2[j-1])

        if (m + n) % 2 == 1:
            return left_max

        if i == m: right_min = nums2[j]
        elif j == n: right_min = num1[i]
        else: right_min = min(nums[i], nums2[j])
        return (left_max + right_min) / 2.0







































class Solution(object):
    def findMedianSortedArrays2(self, nums1, nums2):
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
