class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix: return 0
        if target < matrix[0][0] or target > matrix[-1][-1]: return 0
        m, n = len(matrix), len(matrix[0])
        
        res = 0
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                res += 1
                row, col = row + 1, col - 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return res
                
