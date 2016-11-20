# 63. Unique Paths II  QuestionEditorial Solution  My Submissions
# Total Accepted: 78963
# Total Submissions: 259845
# Difficulty: Medium
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        print(obstacleGrid)
        print("start------")
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize
        A = [[1 for x in xrange(n)] for y in xrange(m)] #Can't use A= [[1]*n] * m. Each element is a reference to the same object which can cause problems 
        print(A)
        
        for i in xrange(1, m):
            print("i : " + str(i))
            if obstacleGrid[i][0] == 1 or A[i-1][0] == 0:
                print(i)
                A[1][0] = 0
        print(A)
        
        for j in xrange(1, n):
            print("j : " + str(j))
            if obstacleGrid[0][j] == 1 or A[0][j-1] == 0:
                A[0][j] = 0
        print(A)
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j]:
                    A[i][j] = 0
                else:
                    A[i][j] = A[i-1][j] + A[i][j-1]
        
        print(A)
        return A[-1][-1]
        

if __name__ == "__main__":
    A = [ [0, 0], [1, 0]]
    Solution().uniquePathsWithObstacles(A)
    
