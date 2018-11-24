# 341. Flatten Nested List Iterator Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 32604
# Total Submissions: 81167
# Difficulty: Medium
# Contributor: LeetCode
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# 
# Example 1:
# Given the list [[1,1],2,[1,1]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# 
# Example 2:
# Given the list [1,[4,[6]]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
# 

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# 2018.11.23
# self wrote
# Use self.L and self.index to keep track of the current Integer
# To find out next,
# First, self.index += 1
# if self.index is pointing to a list, keep looping and adding the current L, index + 1 into stack
# if self.index == len(self.L), pop from stack and find out the next

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.L = nestedList
        self.index = 0
        self.findNext()   # Stop at next INT
            
        

    def next(self):
        """
        :rtype: int
        """
        res = self.L[self.index].getInteger()
        # print("NEXT : ", res)
        self.index += 1
        self.findNext()
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.L else False
        
    def findNext(self):
        # print("findNext : ", self.L, self.index)
        if not self.L and not self.stack:
            return
        
        while self.stack or self.index <= len(self.L):
            if self.index == len(self.L):
                if self.stack:
                    self.L, self.index = self.stack.pop()
                else:
                    self.L = []
            else:
                if self.L[self.index].isInteger():
                    return
                else:
                    self.stack.append([self.L, self.index + 1])
                    self.L = self.L[self.index].getList()
                    self.index = 0
        return 


# 2018.02.25 One stack solution
# First reversely push to stack
# hasNext() to find next available element
# Not a good answer because hasNext is not idempotent

from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.d = deque()
        for i in xrange(len(nestedList) - 1, -1, -1):
            self.d.append(nestedList[i])
        
    def next(self):
        """
        :rtype: int
        """
        return self.d.pop().getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        d = self.d
        #print("hasNext", self.d)
        while d:
            if d[-1].isInteger(): 
                return True
            cur = d.pop().getList()
            for i in xrange(len(cur) - 1, -1, -1):
                d.append(cur[i])
        return False
            

# 2017.05.13 Stack
from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.s = [nestedList, 0]

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return "ERROR"
        nestedList, i = self.s[-1]
        self.s[-1][1] += 1
        return nestedList[i].getInteger()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.s
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.getInterger(): return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
