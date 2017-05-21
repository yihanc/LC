# 346. Moving Average from Data Stream Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 21889
# Total Submissions: 37572
# Difficulty: Easy
# Contributor: LeetCode
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# 
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

# 2017.05.20
# selfwrote
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.d = deque()
        self.sm = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.d) == self.size:
            self.sm = (self.sm - self.d.popleft() + val)
        else:
            self.sm += val
        self.d.append(val)
        return self.sm / float(len(self.d))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
