# 200. Number of Islands Add to List
# Description  Submission  Solutions
# Total Accepted: 92945
# Total Submissions: 281078
# Difficulty: Medium
# Contributors: Admin
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:
# 
# 11110
# 11010
# 11000
# 00000
# Answer: 1
# 
# Example 2:
# 
# 11000
# 11000
# 00100
# 00011
# Answer: 3
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        vis = [ [ False for j in xrange(n) ] for i in xrange(m) ]
        dir = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "0" or vis[i][j]:
                    continue
                
                res += 1
                vis[i][j] = True
                self.dfs(grid, vis, i, j, dir, m, n)
        return res
    
    def dfs(self, grid, vis, i, j, dir, m, n):
        for k in xrange(4):
            x, y = i + dir[k][0], j + dir[k][1]
            
            if x < 0 or y < 0 or x >= m or y >= n or vis[x][y] or grid[x][y] == "0":
                continue
            
            vis[x][y] = True
            self.dfs(grid, vis, x, y, dir, m, n)
            
            
        

