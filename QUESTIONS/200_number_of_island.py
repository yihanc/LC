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

# 2017.05.27 
# Union find
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for row in grid:
            print(row)
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        root = [ x for x in xrange(m * n) ]
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] != "1": continue
#                if root[i * n + j] != i * n + j: continue
                count += 1

                for pair in ([0, 1], [1, 0]):
                    ii, jj = i + pair[0], j + pair[1]
                    print(i, j, ii, jj)
                    if ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj] == "1":
                        x1 = self.find(root, i * n + j )
                        x2 = self.find(root, ii * n + jj )
                        if x1 != x2:
                            count -= 1
                            root[x2] = x1   # better than root[x1] = x2
        return count
                
        

    def find(self, root, id):
        while root[id] != id:
            root[id] = root[root[id]]   # path compression
            id = root[id]
        return id

if __name__ == "__main__":
    # grid = [ "11000", "11000", "00100", "00011" ]
    grid = [ "10100", "01010", "01100", "00011" ]
    print(Solution().numIslands(grid))
    
