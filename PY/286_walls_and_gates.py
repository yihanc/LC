# 286. Walls and Gates Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 29272
# Total Submissions: 67125
# Difficulty: Medium
# Contributor: LeetCode
# You are given a m x n 2D grid initialized with these three possible values.
# 
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
# 
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4


# 2017.05.26
# Scan and BFS
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not len(rooms[0]): return
        m, n = len(rooms), len(rooms[0])
        pairs = [0, 1], [0, -1], [1, 0], [-1, 0]
        
        d = deque()
        vis = [ [False for y in xrange(n)] for x in xrange(m) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    d.appendleft([0, i, j])
                    vis[i][j] = True
        
        while d:
            dep, x, y = d.pop()
            for pair in pairs:
                xx, yy = x + pair[0], y + pair[1]
                if xx < m and xx >= 0 and yy < n and yy >= 0 and rooms[xx][yy] != -1 and not vis[xx][yy]:
                    rooms[xx][yy] = dep + 1
                    vis[xx][yy] = True
                    d.appendleft([dep+1, xx, yy])

                        
                        

