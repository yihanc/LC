# 407. Trapping Rain Water II Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 7205
# Total Submissions: 20076
# Difficulty: Hard
# Contributors: Admin
# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
# 
# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.
# 
# Example:
# 
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# 
# Return 4.
# 
# The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
# 
# 
# After the rain, water are trapped between the blocks. The total volume of water trapped is 4.
# 
# Subscribe to see which companies asked this question.
from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap: return 0
        m, n = len(heightMap), len(heightMap[0])
        
        res, mx = 0, 0
        hq = []
        vis = [ [ False for j in xrange(n) ] for i in xrange(m) ]
        dir = [ [1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heappush(hq, [heightMap[i][j], i, j])
                    vis[i][j] = True
        
        while hq:
            h, xx, yy = heappop(hq)
            mx = max(mx, h)
            
            for i in xrange(4):
                x, y = xx + dir[i][0], yy + dir[i][1]
                if x < 0 or y < 0 or x >= m or y >= n or vis[x][y]:
                    continue
                
                vis[x][y] = True
                if heightMap[x][y] < mx:
                    res += mx - heightMap[x][y]
                
                heappush(hq, [heightMap[x][y], x, y])
        
        return res
                
