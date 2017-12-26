# 28. Search a 2D Matrix 
# Write an efficient algorithm that searches for a value in an m x n matrix.
# 
# This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Have you met this question in a real interview? Yes
# Example
# Consider the following matrix:
# 
# [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here

        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[mid//n][mid%n]:
                return True
            elif target > matrix[mid//n][mid%n]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
                
