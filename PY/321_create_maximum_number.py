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


# 2017.05.15
# https://www.hrwhisper.me/leetcode-create-maximum-number/
# others idea
# function1 : get_max_sub_array(), from nums, get biggest subarray size k with same order
# function2: greater(), compare two same size nums[], return True if nums1 is greater
# main() i = # of elements from nums1, so that k - i = # of elements from nums2
# 
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [ 0 for _ in xrange(k) ]
        for i in xrange(max(k-len(nums2), 0), min(len(nums1), k) + 1):  # i is the # of element from nums1
            res1 = self.get_max_sub_array(nums1, i)     # res1 = i max sub from nums1
            res2 = self.get_max_sub_array(nums2, k - i) # res2 = k-i max elements from nums2
            res = self.merge(res1, res2)  # for holding cur result of i
            if not self.greater(ans, 0, res, 0):
                ans = res
        return ans
    
    def merge(self, nums1, nums2):  # Merging two lists to get max possible
        res = [ 0 for _ in xrange(len(nums1) + len(nums2)) ]
        pos1, pos2, tpos = 0, 0, 0
        while pos1 < len(nums1) and pos2 < len(nums2):
            if self.greater(nums1, pos1, nums2, pos2):  # run greater to decide which num to pick
                res[tpos] = nums1[pos1]
                pos1 += 1
            else:
                res[tpos] = nums2[pos2]
                pos2 += 1
            tpos += 1
        res[tpos:] = nums1[pos1:] if pos2 == len(nums2) else nums2[pos2:]
        return res
    
    def greater(self, nums1, start1, nums2, start2):    # min(m, n)
        while start1 < len(nums1) and start2 < len(nums2):
            if nums1[start1] > nums2[start2]: return True
            if nums1[start1] < nums2[start2]: return False
            start1, start2 = start1 + 1, start2 + 1
        return start1 != len(nums1)
        
    def get_max_sub_array(self, nums, k):
        res = [ 0 for _ in xrange(k) ]
        le = 0   # j is the len of res)
        for i in xrange(len(nums)):
            while le > 0 and le + len(nums) - i > k and res[-1] < nums[i]:
                le -= 1
            if le < k:
                res[le] = nums[i]
                le += 1
        return res
