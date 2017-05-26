# 463. Island Perimeter Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 38653
# Total Submissions: 67952
# Difficulty: Easy
# Contributors:
# amankaraj
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

# 2017.05.23
# Math
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        ilds, nbrs = 0, 0
        res = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1: 
                    ilds += 1
                    if i + 1 < m and grid[i+1][j] == 1: nbrs += 1
                    if j + 1 < n and grid[i][j+1] == 1: nbrs += 1
                
        return ilds * 4 - nbrs * 2
                
