# 505. The Maze II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 3479
# Total Submissions: 9703
# Difficulty: Medium
# Contributors:
# ganbatte
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# 
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
# 
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
# 
# Example 1
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# 
# Output: 12
# Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
#              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
# 
# Example 2
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
# 
# Output: -1
# Explanation: There is no way for the ball to stop at the destination.
# 
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# 2017.05.27
# no vis
# adding [lenth] info into 
from collections import deque

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]: return -1
        m, n = len(maze), len(maze[0])
        pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        routes = [ [ m * n for y in xrange(n) ] for x in xrange(m) ]
        
        d = deque()
        d.append(start + [0])

        while d:
            x, y, dep = d.pop()
            if routes[x][y] <= dep: continue
            routes[x][y] = dep
            
            for pair in pairs:
                xx, yy, l = x, y, dep
                while xx >= 0 and xx < m and yy >= 0 and yy < n and maze[xx][yy] == 0:
                    xx += pair[0]
                    yy += pair[1]
                    l += 1
                xx -= pair[0]       # Valid point before wall
                yy -= pair[1]
                l -= 1
                d.appendleft([xx, yy, l])
        return routes[destination[0]][destination[1]] if routes[destination[0]][destination[1]] != m * n else -1
                
            
        

