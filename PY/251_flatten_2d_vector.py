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

# 2018.02.24
# Initiate i, j to the first valid element
# when calling next(), save the res, move the pointer to next valid, return output
# When calling hasNext, as long as it is not the last position, i == len(v), j == 0
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v = vec2d
        self.i, self.j = 0, 0
        while self.i < len(self.v) and self.j >= len(self.v[self.i]):       # In case v[0] is empty list
            self.i += 1

    def next(self):
        """
        :rtype: int
        """
        v = self.v
        res = v[self.i][self.j]
        self.j += 1
        while self.i < len(v) and self.j >= len(v[self.i]):
            self.i, self.j = self.i + 1, 0
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        v = self.v
        return not (self.i == len(v) and self.j == 0)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


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
