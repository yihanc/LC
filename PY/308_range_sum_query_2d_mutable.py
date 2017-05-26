# 308. Range Sum Query 2D - Mutable Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 13925
# Total Submissions: 64286
# Difficulty: Hard
# Contributor: LeetCode
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# 
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
# 
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

# 2017.05.21
# 2D BI Tree
# Draw a 2D diagram
# 
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [ [0 for j in xrange(self.n+1) ] for i in xrange(self.m+1)]
        self.nums = [ [0 for j in xrange(self.n)] for i in xrange(self.m) ]
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i, j, matrix[i][j])
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        def _sum(row, col):
            res = 0
            i = row + 1
            while i > 0:
                j = col + 1
                while j > 0:
                    res += self.tree[i][j]
                    j -= j & -j
                i -= i & -i
            return res
        
        return _sum(row2, col2) - _sum(row2, col1-1) - _sum(row1-1, col2) + _sum(row1-1, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
