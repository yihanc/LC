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

# 2018.04.08 recursive path compression
# Note that, when unioning, 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        roots = [ i for i in xrange(m * n) ]
        
        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                #print(i, j, "cnt", cnt, roots)

                if grid[i][j] == "0": continue
                
                r1 = self.find(roots, i * n + j)
                cnt += 1
                for pair in [[0, -1], [-1, 0]]:
                    xx, yy = i + pair[0], j + pair[1]
                    if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == "1":
                        r2 = self.find(roots, xx * n + yy)
                        if r1 != r2:
                            roots[r2] = r1
                            cnt -= 1
        return cnt      
                        
    
    def find(self, roots, x):
        if roots[x] != x:
            roots[x] = self.find(roots, roots[x])       # Paths compression
        return roots[x]

# 2018.02.22
# Union Find
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        roots = [ x for x in xrange(m * n)]
        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "0": continue
                r1 = self.find(roots, i * n + j)
                cnt += 1
                for pair in ((0, -1), (-1, 0)):
                    ii, jj = i + pair[0], j + pair[1]
                    if ii >= 0 and jj >= 0 and grid[ii][jj] == "1":
                        r2 = self.find(roots, ii * n + jj)
                        if r1 != r2:
                            roots[r2] = r1
                            cnt -= 1
        return cnt
                
    
    def find(self, roots, i):
        while roots[i] != i:
            roots[i] = roots[roots[i]]
            i = roots[i]
        return roots[i]

# 2017.05.27 
# Union find
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not len(grid[0]): return 0
        m, n = len(grid), len(grid[0])
        print("m, n, : ", m, n)
        
        roots = [ x for x in xrange(m * n)]
        count = 0
        pairs = [[0, 1], [1, 0]]        # only searching right and down.
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "0": continue
            
                x = self.find(roots, i * n + j) # i,j 's parent
                
                count += 1
                for pair in pairs:
                    ii, jj = i + pair[0], j + pair[1]
                    if ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj] == "1":
                        y = self.find(roots, ii * n + jj)

                        if x != y:              # isolated. union them
                            roots[y] = x        # not roots[x] = y
                            count -= 1
        return count
    
    def find(self, roots, id):
        while roots[id] != id:
            roots[id] =  roots[roots[id]]
            id = roots[id]
        return id
                

# 2017.03.25 Rewrite. DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        
        res = 0
        vis = [[ False for y in xrange(n) ] for x in xrange(m) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if not vis[i][j] and grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j, vis, m, n)
        return res
    
    def dfs(self, grid, i, j, vis, m, n):
        vis[i][j] = True
        pairs = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        
        for pair in pairs:
            x, y = i + pair[0], j + pair[1]
            if x >= 0 and y >= 0 and x < m and y < n and not vis[x][y] and grid[x][y] == "1":
                self.dfs(grid, x, y, vis, m, n)


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
            
            
        

