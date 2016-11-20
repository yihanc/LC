# 62. Unique Paths  QuestionEditorial Solution
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.

# Math solution too..
# DP Matrix
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        #A = [[1] * n ] * m     This is wrong
        A = [[1 for x in xrange(n)] for y in xrange(m)]
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                A[i][j] = A[i-1][j] + A[i][j-1]
        
        return A[-1][-1]
        
if __name__ == "__main__":
    Solution().uniquePaths(2, 2)
    
