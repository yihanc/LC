# 48. Rotate Image   QuestionEditorial Solution  My Submissions
# Total Accepted: 85790
# Total Submissions: 234890
# Difficulty: Medium
# Contributors: Admin
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.flipUpDown(matrix)
#        for i in xrange(len(matrix)):
#            print matrix[i]
        self.flipDiagonal(matrix)
    
    def flipUpDown(self, matrix):
        if len(matrix) <= 1:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        for i in xrange(m//2):      # Watch out the range
            for j in xrange(n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[m-i-1][j]
                matrix[m-i-1][j] = tmp
    
    def flipDiagonal(self, matrix):
        if len(matrix) <= 1:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        for i in xrange(1, m):
            for j in xrange(0, i):  # Watch out the range
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp 

if __name__  == "__main__":
    #matrix = [[ 1,2,3], [4,5,6], [7,8,9]]
    matrix = [[1,2], [3,4]]
    Solution().rotate(matrix)
    for i in xrange(len(matrix)):
        print matrix[i]
