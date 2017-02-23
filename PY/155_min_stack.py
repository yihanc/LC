# 155. Min Stack
# Description  Submission  Solutions  Add to List
# Total Accepted: 111449
# Total Submissions: 418153
# Difficulty: Easy
# Contributors: Admin
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# Subscribe to see which companies asked this question.
import sys
from collections import deque

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minn = sys.maxint
        self.d = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.d:
            self.d.append(0)
            self.minn = x
        else:
            self.d.append(x - self.minn)
            if x < self.minn:
                self.minn = x

    def pop(self):
        """
        :rtype: void
        """
        if not self.d:
            return
        else:
            if self.d[-1] < 0:
                self.minn = self.minn - self.d[-1]
            self.d.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.d:
            return self.minn
        else:
            if self.d[-1] < 0:
                return self.minn
            else:
                return self.minn + self.d[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minn
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
