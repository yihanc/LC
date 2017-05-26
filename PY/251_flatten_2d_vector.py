# 251. Flatten 2D Vector Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23819
# Total Submissions: 59688
# Difficulty: Medium
# Contributor: LeetCode
# Implement an iterator to flatten a 2d vector.
# 
# For example,
# Given 2d vector =
# 
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
# 
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.


# 2017.05.26
# Another solution using i,j
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i, self.j = 0, 0
        while self.i != len(self.vec2d) and self.j == len(self.vec2d[self.i]):
            self.i += 1
            self.j = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            cur = self.vec2d[self.i][self.j]
            self.j += 1
            while self.i != len(self.vec2d) and self.j == len(self.vec2d[self.i]):
                self.i += 1
                self.j = 0
            return cur

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.i < len(self.vec2d) and self.j < len(self.vec2d[self.i]) else False


# 2017.05.26
# Use a list and index
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.L = []
        for row in vec2d:
            self.L += row
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            self.i += 1
            return self.L[self.i-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i != len(self.L)
