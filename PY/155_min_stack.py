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

# 2017.03.06 Self write
# Use a self.min to keep track
# Pushing:
# If x >= min, add x - min (positive) in the stack
# If x < min, update min, add x - min (min) in the stack
# Popping:
# If stack[-1] >= 0, just pop() no update needed.
# If stack[-1] < 0, update min = min - stack[-1]
# Top:
# If  stack[-1] >= 0, return min + stack[-1]
# else: return min

import sys
from collections import deque
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.curMin = sys.maxint 
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.curMin = x
            self.stack.append(0)
        elif x >= self.curMin:
            self.stack.append(x - self.curMin)
        else:
            self.stack.append(x - self.curMin)
            self.curMin = x
            
        
    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:  return
        if self.stack[-1] < 0:
            self.curMin -= self.stack[-1]
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack: return sys.maxint
        if self.stack[-1] < 0: 
            return self.curMin
        else:
            return self.curMin + self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.curMin

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
