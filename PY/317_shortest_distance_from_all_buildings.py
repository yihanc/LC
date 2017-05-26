# 317. Shortest Distance from All Buildings Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 15464 Total Submissions: 45917 Difficulty: Hard Contributor: LeetCode
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
# 
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
# 
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.


# 2017.05.23
# BFS + counter

from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        mindist = [ [ 0 for y in xrange(n)] for x in xrange(m) ]
        res = float('inf')
        
        start = 0       # Counter to track how many 1 is there
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    d = deque()
                    d.append([0, i, j])
                    while d:
                        dep, x, y = d.pop()
                        for pair in pairs:
                            xx, yy = x + pair[0], y + pair[1]
                            if xx < m and xx >= 0 and yy < n and yy >= 0 and grid[xx][yy] == start:
                                grid[xx][yy] -= 1
                                mindist[xx][yy] += dep + 1
                                d.appendleft([dep + 1, xx, yy])
                    start -= 1
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == start: res = min(res, mindist[i][j])
        return res if res != float('inf') else -1
                            
                        

