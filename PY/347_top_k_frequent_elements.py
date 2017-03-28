#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 347. Top K Frequent Elements
# Description  Submission  Solutions  Add to List
# Total Accepted: 49405
# Total Submissions: 106489
# Difficulty: Medium
# Contributors: Admin
# Given a non-empty array of integers, return the k most frequent elements.
# 
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Subscribe to see which companies asked this question.

# 2017.03.25 Heapq
from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:        # O(N)
            dic[num] = dic.get(num, 0) + 1
        
        hq = []
        for key, value in dic.iteritems():  # heappush worst n logn
            heappush(hq, [-value, key])
        
        res = []
        for i in xrange(k):     
            res.append(heappop(hq)[1])
        return res

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        fre = [[] for x in xrange(n+1) ]
        dic = {}
        res = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        for key, value in dic.iteritems():
            fre[value].append(key)
        
        print(dic)
        print(fre)
        
        i = n
        while i >= 0:
            if len(fre[i]) > 0 and len(fre[i]) <= k:
                res = res + fre[i]
                k -= len(fre[i])
                if k == 0: return res
            elif len(fre[i]) > 0 and len(fre[i]) > k:
                res = res + fre[i][:k]
                return res
            i -= 1

if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3]
    print(Solution().topKFrequent(nums, 2))
