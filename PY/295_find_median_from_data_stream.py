# 295. Find Median from Data Stream Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 39442
# Total Submissions: 156057
# Difficulty: Hard
# Contributor: LeetCode
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# 
# Examples: 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# 2017.05.14 
# online two minheap solution
# Steps:
# 1. insert nums to large
# 2. pop large and insert -x to smalls
# 3. if len(large) < len(small), pop small and then add to large so that len(large) >= len(small)

from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        return (-small[0] + large[0]) / 2.0

# 2017.05.14 Naive list method
# Failed for last large case
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.nums.append(num)
        self.nums.sort()
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        return self.nums[n//2] if n & 1 else (self.nums[n//2-1] + self.nums[n//2]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
