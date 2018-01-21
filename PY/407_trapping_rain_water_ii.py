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

# 2018.01.15 Heapq + BFS
# 1. Add all sides into heapq and mark visited before pushing into heapq
# 2. Pop one from hq, and process its neighbor
# 3. Update vis, update res, push into hq (with original value so that it can be processed early), update value to the parent


# 2017.05.11 DFS
# 1. First scan sides and push them into heapq
# 2. while hq, pop and check his side cells, if unvisited. 
from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap: return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3: return 0
        vis = [ [ False for j in xrange(n)] for i in xrange(m) ]
        res = 0
        hq = []
        for j in xrange(n):
            heappush(hq, (heightMap[0][j], 0, j))
            heappush(hq, (heightMap[m-1][j], m-1, j))
            vis[0][j] = True
            vis[m-1][j] = True
            
        for i in xrange(1, m - 1):
            heappush(hq, (heightMap[i][0], i, 0))
            heappush(hq, (heightMap[i][n-1], i, n - 1))
            vis[i][0] = True
            vis[i][n-1] = True
        
        while hq:
            cur, x, y = heappop(hq)
            pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            #print(hq)
            for pair in pairs:
                xx, yy = x + pair[0], y + pair[1]
                if xx < m and xx >= 0 and yy < n and yy >= 0 and not vis[xx][yy]:
                    vis[xx][yy] = True
                    heappush(hq, (heightMap[xx][yy], xx, yy))
                    res += max(0, heightMap[x][y] - heightMap[xx][yy])

                    #print((x,y), (xx, yy), res, heightMap[x][y], heightMap[xx][yy])
                    heightMap[xx][yy] = max(heightMap[x][y], heightMap[xx][yy])
                    
        return res



# Using a heapq to process
# From the outside, Always process the lowest point  
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
                
