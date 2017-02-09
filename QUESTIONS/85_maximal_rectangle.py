# 85. Maximal Rectangle  QuestionEditorial Solution  My Submissions
# Total Accepted: 50686
# Total Submissions: 202962
# Difficulty: Hard
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
# Subscribe to see which companies asked this question
from collections import deque

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        heights = [ [ 0 for j in xrange(n + 1) ] for i in xrange(m) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and matrix[i][j] == "1":
                    heights[i][j] = 1
                elif matrix[i][j] == "1":
                    heights[i][j] += heights[i-1][j] + 1
                else:
                    pass
        print(heights)
        
        for i in xrange(m):
            d = deque()
            for j in xrange(n + 1):
                while d and heights[i][j] < heights[i][d[-1]]:
                    index = d.pop()
                    h = heights[i][index]
                    l = -1 if not d else d[-1]
                    side = j - l - 1
                    res = max(res, h * side)
                    print(i, j, h, side, res)
                d.append(j)
                
        return res
        
        

if __name__ == "__main__":
    A = ["10100","10111","11111","10010"]
    print("A", A)
    print(Solution().maximalRectangle(A))


