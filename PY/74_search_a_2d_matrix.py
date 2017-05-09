# 74. Search a 2D Matrix  QuestionEditorial Solution  My Submissions
# Total Accepted: 94152
# Total Submissions: 268488
# Difficulty: Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

# 2017.05.06 same idea as Search ii
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = start + ( end - start ) // 2

            #Calculate coordinates
            v_mid = matrix[mid // n][mid % n]

            if v_mid == target:
                return True
            elif v_mid > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False

# Test cases:
# [[0]] 0
# [[0]] 1
# [[1,2,3]] 3
# [[1,2,3], [4,5,6]] 5
