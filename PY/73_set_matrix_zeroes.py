# 73. Set Matrix Zeroes   QuestionEditorial Solution  My Submissions
# Total Accepted: 82389
# Total Submissions: 236922
# Difficulty: Medium
# Contributors: Admin
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# 
# click to show follow up.
# 
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# 
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        row0, col0 = False, False
        
        for j in xrange(n):
            if matrix[0][j] == 0:
                row0 = True
        
        for i in xrange(m):
            if matrix[i][0] == 0:
                col0 = True
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if i != 0 and j != 0 and matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for j in xrange(1,n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0
        
        for i in xrange(1,m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0
        
        if row0:
            for j in xrange(n):
                matrix[0][j] = 0
            
        if col0:
            for i in xrange(m):
                matrix[i][0] = 0
        
if __name__ == "__main__":
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    for row in matrix:
        print(row)
    Solution().setZeroes(matrix)
    print("----------------")
    for row in matrix:
        print(row)
