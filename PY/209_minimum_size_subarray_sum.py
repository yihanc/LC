# 209. Minimum Size Subarray Sum Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 72698
# Total Submissions: 247761
# Difficulty: Medium
# Contributors: Admin
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# click to show more practice.
# 
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# 2017.03.12 Moving window

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, 0
        
        res = n + 1
        csum = 0
        while r <= n:
            #print(csum, l, r)
            if csum >= s:
                res = min(res, r - l)
                csum -= nums[l]
                l += 1
                continue
            
            if r < n:
                csum += nums[r]
            r += 1
            
        return res if res != n + 1 else 0
            
        
