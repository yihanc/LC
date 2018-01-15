# 321. Create Maximum Number Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 17173
# Total Submissions: 70587
# Difficulty: Hard
# Contributor: LeetCode
# Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.
# 
# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
# 
# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]
# 
# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        m, n = len(nums1), len(nums2)
        # i >= 0, i <= m, k -i >= 0,( i<= k),  k -i <= n ( i>= k -n )
        for i in xrange(max(0, k - n), min(m, k) + 1):
#             print("---- Fetching i from nums1", i)
            can1 = self.maxArray(nums1, i)
            can2 = self.maxArray(nums2, k - i)
            cand = self.merge(can1, can2)
#             print(can1, can2, cand)
            if not res or (cand > res):
                res = cand
        return res
            
    def maxArray(self, nums, k):    # Get K maximum from nums
        res = [ 0 for j in xrange(k) ]

        pos = -1 # Last index
        for j in xrange(k): # j pointer for res, i pointer in nums
#            print("------ ", j)
            left = k - j    # Still need to find left elements
            i = pos + 1
#            print("Inside len(nums), i, left, len(nums) ",len(nums),  i, left)
            while len(nums) - i >= left:
                if nums[i] > res[j]:
                    res[j] = nums[i]
                    pos = i
#                    print("HERE i j pos", i, nums[i],  j, res[j],  pos)
                i += 1
#                print(res)
        return res
    
    def merge(self, nums1, nums2):
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        res = []
        while i < m and j < n:
#            if nums1[i] == nums2[j]:        # BUG
 #               if nums1[i+1:] > nums2[j+1:]:
            if nums1[i] > nums2[j] or (nums1[i] == nums2[j] and nums1[i+1:] > nums2[j+1:]):
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        return res + nums2[j:] if i == m else res + nums1[i:]
        
            
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3

nums1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
nums2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
k = 300
print(nums1)
print(nums2)
print(Solution().maxNumber(nums1, nums2, k))
