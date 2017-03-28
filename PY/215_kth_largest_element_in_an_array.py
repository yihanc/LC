# 215. Kth Largest Element in an Array Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 116462
# Total Submissions: 305218
# Difficulty: Medium
# Contributors: Admin
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# 2017.03.25 sort and index. nlogn + 1
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()     # nlogn
        return nums[-k]     # 1

# 2017.03.12 Priority queue. O(N) + k. heappush is log(n), so it is nlogn + k
from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hq = []
        for num in nums:
            heappush(hq, -num)
        
        while k > 1:
            heappop(hq)
            k -= 1
        return -hq[0]

# 2017.03.12 Simple sort O(nlgn)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
        

