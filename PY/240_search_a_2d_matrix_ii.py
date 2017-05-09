# 240. Search a 2D Matrix II  QuestionEditorial Solution  My Submissions
# Total Accepted: 50065
# Total Submissions: 136839
# Difficulty: Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# 
# Given target = 20, return false.
#

# 85ms. worst case o(n + m), best()
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False

# 2017.05.06 self wrote
# worst case, mlog(n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        if n == 0: return False
        for i in xrange(m):
            if target < matrix[i][0]  or target > matrix[i][-1] : continue
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
