# 239. Sliding Window Maximum Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 57056
# Total Submissions: 176677
# Difficulty: Hard
# Contributor: LeetCode
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
# 
# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
# 
# 

# 2017.05.06 Deque o(n) solution
# traverse nums
# check deque:
# if the leftmax < window left: popleft
# while d right index < : popright
# so that d[0] is always the biggest
# add index to deque and append res
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0: return []
        res = []
        n = len(nums)
        d = deque()
        for i in xrange(n):
            while d and d[0] <= i - k: d.popleft()
            while d and nums[d[-1]] < nums[i]: d.pop()
            d.append(i)
            if i >= k - 1:
                res.append(nums[d[0]])
        return res
                


# Naive o(k * (n - k + 1)) solution
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0: return []
        res = []
        n = len(nums)
        for i in xrange(n - k + 1):
            res.append(max(nums[i:i+k]))
        return res
