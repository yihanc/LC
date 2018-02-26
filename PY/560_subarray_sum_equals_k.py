# 560. Subarray Sum Equals K
# DescriptionHintsSubmissionsDiscussSolution
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


# 2018.02.25 Hash table
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = defaultdict(int)
        csum = 0
        dic[csum] = 1
        cnt = 0
        for num in nums:
            csum += num
            if csum - k in dic:
                cnt += dic[csum-k]
            dic[csum] += 1
        return cnt
            
        
            


# 2018.02.25 TLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        psum = [ 0 for i in xrange(n + 1)]
        for i in xrange(n):
            psum[i+1] = psum[i] + nums[i]
        #print(psum)
        res = 0
        for i in xrange(n):
            for j in xrange(i + 1, n + 1):
                if psum[j] - psum[i] == k:
                    res += 1
        return res
