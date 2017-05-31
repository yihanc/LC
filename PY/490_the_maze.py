# 490. The Maze Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 4007
# Total Submissions: 9422
# Difficulty: Medium
# Contributors:
# fallcreek
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# 
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
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
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
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
# Output: false
# Explanation: There is no way for the ball to stop at the destination.
# 
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# Two tricky points. 
# when to update vis? only when hitting a wall.
# BFS or DFS? BFS seems easier.

# 2017.05.27
# Others BFS solution
from collections import deque
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]: return False
        m, n = len(maze), len(maze[0])
        pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        d = deque()
        d.append(start)
        vis = set([start[0] * n + start[1]])
        
        while d:
            x, y = d.pop()
            
            for pair in pairs:
                xx, yy = x, y
                while xx >= 0 and xx < m and yy >= 0 and yy < n and maze[xx][yy] == 0:
                    xx += pair[0]
                    yy += pair[1]
                xx -= pair[0]       # Valid point before wall
                yy -= pair[1]
                if xx * n + yy in vis: continue
                vis.add(xx * n + yy)
                if [xx, yy] == destination: return True
                d.appendleft([xx, yy])
        return False
                
            
        


# 2017.05.27
# Self wrote. 
# DFS + vis
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]: return False
        m, n = len(maze), len(maze[0])
        dic = {
            "U": [-1, 0],
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1]
        }
        x, y = start
        for d in "RDLU":
            xx, yy = x + dic[d][0], y + dic[d][1]
            vis = set()
            if xx >= m or xx < 0 or yy >= n or yy < 0 or maze[xx][yy] == 1: continue
            if self.dfs(maze, xx, yy, destination, d, dic, vis): return True
        return False
        
        
    def dfs(self, maze, x, y, des, dir, dic, vis):
        #print(x, y, dir, vis)
        m, n = len(maze), len(maze[0])
        if str(x * n + y) + dir in vis: return
    
        vis.add(str(x * n + y) + dir)       # add direction to the vis
        xx, yy = x + dic[dir][0], y + dic[dir][1]
        hitwall = True if xx >= m or xx < 0 or yy >= n or yy < 0 or maze[xx][yy] == 1 else False
        #print("hitwall: ", hitwall, [x, y], des)
        if hitwall and [x, y] == des:
            #print("RESULT GET")
            return True
        
        if not hitwall:
            if self.dfs(maze, xx, yy, des, dir, dic, vis): return True
        else:
            directions = "RL" if dir in "UD" else "DU"
            for d in directions:
                xx, yy = x + dic[d][0], y + dic[d][1]
                if xx >= m or xx < 0 or yy >= n or yy < 0 or maze[xx][yy] == 1 or str(xx * n + yy) + d in vis: continue
                if self.dfs(maze, xx, yy, des, d, dic, vis): return True
        return False


        
        


# Cases
# [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# [0,4]
# [3,2]

# [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
# [0,0]
# [8,6]
