# 304. Range Sum Query 2D - Immutable Add to List
# Description
# Hints
# Submissions
# Solutions
# Total Accepted: 30776 Total Submissions: 127359 Difficulty: Medium
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
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 

# 2017.05.21
# BI Tree

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[ 0 for y in xrange(self.n + 1)] for x in xrange(self.m + 1) ]
        i = 1
        
        for i in xrange(self.m):
            for j in xrange(self.n):
                row = i + 1
                while row <= self.m:
                    col = j + 1
                    while col <= self.n:
                        self.tree[row][col] += matrix[i][j]
                        col += col & -col
                    row += row & -row

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
        
        return _sum(row2, col2) - _sum(row2, col1 - 1) - _sum(row1-1, col2) + _sum(row1-1, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
