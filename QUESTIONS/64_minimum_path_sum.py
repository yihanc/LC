# 64. Minimum Path Sum  QuestionEditorial Solution  My Submissions
# Total Accepted: 85653
# Total Submissions: 234994
# Difficulty: Medium
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Subscribe to see which companies asked this question
# 
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        A = [[0 for x in xrange(n)] for y in xrange(m)]
        A[0][0] = grid[0][0]
        
        for i in xrange(1, m):
            A[i][0] = A[i-1][0] + grid[i][0]
        
        for j in xrange(1, n):
            A[0][j] = A[0][j-1] + grid[0][j]
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                A[i][j] = min(A[i-1][j], A[i][j-1]) + grid[i][j]
        
        return A[-1][-1]

if __name__ == "__main__":
    grid = [[1,2,5],[3,2,1]]
    Solution().minPathSum(grid)
