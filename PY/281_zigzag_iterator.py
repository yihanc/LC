# 281. Zigzag Iterator Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 24907
# Total Submissions: 50119
# Difficulty: Medium
# Contributor: LeetCode
# Given two 1d vectors, implement an iterator to return their elements alternately.
# 
# For example, given two 1d vectors:
# 
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
# 
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
# 
# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:
# 
# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].

# 2017.05.21 
# Queue solution
from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.dq = deque()
        if v1: self.dq.appendleft(v1)
        if v2: self.dq.appendleft(v2)
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext: v = self.dq.pop()
        val = v.pop(0)  # This is slow for popping the first ele from list
        if v: self.dq.appendleft(v)
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.dq else False


# 2017.05.21
# self wrote
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1, self.v2 = v1, v2
        self.i1, self.i2 = 0, 0
        
    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext: return
        if self.i1 < len(self.v1) and (self.i1 == self.i2 or self.i2 == len(self.v2)):
            self.i1 += 1
            return self.v1[self.i1-1]
        else:
            self.i2 += 1
            return self.v2[self.i2-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i1 < len(self.v1) or self.i2 < len(self.v2):
            return True
        return False
