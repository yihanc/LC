# 361. Bomb Enemy Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14111
# Total Submissions: 36526
# Difficulty: Medium
# Contributor: LeetCode
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
# 
# Example:
# For the given grid
# 
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# 
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.


# 2017.05.21
# When scanning. Memorizing rowhits and colhits
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        rowhits, colhits = 0, [0 for j in xrange(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                if j == 0 or grid[i][j-1] == 'W':   # Update rowhits only at first col and after 'W'
                    rowhits = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'W': break
                        if grid[i][k] == 'E': rowhits += 1
                
                if i == 0 or grid[i-1][j] == 'W' : # Update colhits only at first row and after 'W'
                    colhits[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] =="W": break
                        if grid[k][j] == 'E': colhits[j] += 1
                
                if grid[i][j] == '0':
                    res = max(res, rowhits + colhits[j])
        return res


# 2017.05.21
# Violence, m * n * (m + n)
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '0':
                    res = max(res, self.bomb(grid, i, j))
        return res
    
    def bomb(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        ii, jj = i + 1, j
        while ii < m:
            if grid[ii][jj] == 'W': break
            if grid[ii][jj] == 'E': cnt += 1
            ii += 1
        
        ii, jj = i - 1, j
        while ii >= 0:
            if grid[ii][jj] == 'W': break
            if grid[ii][jj] == 'E': cnt += 1
            ii -= 1
        
        ii, jj = i, j + 1
        while jj < n:
            if grid[ii][jj] == 'W': break
            if grid[ii][jj] == 'E': cnt += 1
            jj += 1        
            
        ii, jj = i, j - 1
        while jj >= 0:
            if grid[ii][jj] == 'W': break
            if grid[ii][jj] == 'E': cnt += 1
            jj -= 1
        return cnt
            
        
