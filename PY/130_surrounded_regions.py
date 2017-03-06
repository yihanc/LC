# 130. Surrounded Regions   QuestionEditorial Solution  My Submissions # Total Accepted: 66921
# Total Submissions: 390322
# Difficulty: Medium
# Contributors: Admin
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# Subscribe to see which companies asked this question


# BFS Algorithms:
# 1. Scan bondaries and appendleft to deque()
# 2. pop, check adjancet and push to deque()
# 3. Rescan mid board and flip not in isVis

# 2017.02.22 BFS
from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2: return 
        d = deque()

        visited = [ [ False for j in xrange(n) ] for i in xrange(m) ]
        
        for j in xrange(n):
            if board[0][j] == 'O' and not visited[0][j]:
                d.appendleft([0, j])

            if board[m-1][j] == 'O' and not visited[m-1][j]:
                d.appendleft([m - 1, j])

        for i in xrange(1, m-1):
            if board[i][0] == 'O' and not visited[i][0]:
                d.appendleft([i, 0])

            if board[i][n-1] == 'O' and not visited[i][n-1]:
                d.appendleft([i, n - 1])
                
        while d:
            i, j = d.pop()
            visited[i][j] = True

            if i + 1 < m and board[i+1][j] == 'O' and not visited[i+1][j]:
                d.appendleft([i + 1, j])
            if j + 1 < n and board[i][j+1] == 'O' and not visited[i][j+1]:
                d.appendleft([i, j + 1])
            if i - 1 >= 0 and board[i-1][j] == 'O' and not visited[i-1][j]:
                d.appendleft([i-1, j])
            if j - 1 >= 0 and board[i][j-1] == 'O' and not visited[i][j-1]:
                d.appendleft([i, j-1])            

        for i in xrange(1, m - 1):
            for j in xrange(1, n - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

        return

# 12.06.2016 Rewrite. DFS cannot pass the new test case. Need to review to BFS
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2: return

        starts = []
        visited = [[ False for j in xrange(n)] for i in xrange(m)]

        for j in xrange(n):
            if board[0][j] == 'O':
                visited[0][j] = True
                starts.append([0, j])
            if board[m-1][j] == 'O':
                visited[m-1][j] = True
                starts.append([m-1, j])

        for i in xrange(1, m-1):
            if board[i][0] == 'O':
                visited[i][0] = True
                starts.append([i, 0])
            if board[i][n-1] == 'O':
                visited[i][n-1] = True
                starts.append([i, n-1])

        for i, j in starts:
            self.dfs(board, visited, i, j, m, n)

        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X' 

        return


    def dfs(self, board, visited, i, j, m, n):
        neighbors = []

        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if (x >= 0 and y >= 0 and x < m and y < n and not visited[x][y] and board[x][y] == 'O'):
                neighbors.append([x, y])

        for x, y in neighbors:
            visited[x][y] = True
            self.dfs(board, visited, x, y, m, n)

# Notes:
# 'O' not 0
# OJ input is list

# BFS deque solution
from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 1. Record all boundaries in deque.
        if not board: return                # Corner case
        d = deque()
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:                # Corner case
            return
        
        isVis = [ [False for j in xrange(n)] for i in xrange(m)]
        
        for j in xrange(n):
            if board[0][j] == 'O': d.appendleft([0, j])
            if board[m-1][j] == 'O': d.appendleft([m-1, j])
        
        for i in xrange(1, m-1):
            if board[i][0] == 'O': d.appendleft([i, 0])
            if board[i][n-1] == 'O': d.appendleft([i, n-1])
        
        # 2. For each deque. visit adjancent. mark them in isVis[][]
        while d:
            print(d)
            i, j = d.pop()
            if isVis[i][j]:
                continue
            
            if i + 1 < m and board[i+1][j] == 'O' and not isVis[i+1][j]:
                d.appendleft([i+1, j])
            if i - 1 >= 0 and board[i-1][j] == 'O' and not isVis[i-1][j]:
                d.appendleft([i-1, j])
            if j + 1 < n and board[i][j+1] == 'O' and not isVis[i][j+1]:
                d.appendleft([i, j+1])
            if j - 1 >= 0 and board[i][j-1] == 'O' and not isVis[i][j-1]:
                d.appendleft([i, j-1])
        
            isVis[i][j] = True    
        
        # 3. scan inside board. if not in visited. 
        for j in xrange(1, n-1):
            for i in xrange(1, m-1):
                if board[i][j] == 'O' and not isVis[i][j]: 
                    board[i] = board[i][:j] + 'X' + board[i][j+1:]
                    #board[i][j] = 'X'  #If each line is list
                    
        return        
        

if __name__ == "__main__":
    board = ["OXO","XOX","OXO"]
#    board = ["XXXX","XOOX","XXOX","XOXX"]
    board = ["OXOOOX","OOXXXO","XXXXXO","OOOOXX","XXOOXO","OOXXXX"]
    for row in board:
        print([ row])
    Solution().solve(board)
    for row in board:
        print([ row])


### DFS maximum recursion depth exceeded
# See if '0' is attached to edge.
# class Solution2(object):
#     def solve(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
#         if not board: 
#             return
#         
#         m, n = len(board), len(board[0])    #Special cases, if m or n <= 2. return all XXX
#         candidates = []                      #i, j
#         isVisited = [[ False for j in xrange(n)] for i in xrange(m)]
# 
#         # Scan all sides and get candidates
#         for j in xrange(n):
#             if board[0][j] == 'O':
#                 candidates.append([0, j])
#             if m == 1:
#                 break
#             if board[m-1][j] == 'O':
#                 candidates.append([m-1, j])
#         
#         for i in xrange(m):
#             if board[i][0] == 'O':
#                 candidates.append([i, 0])
#             if n == 1:
#                 break
#             if board[i][n-1] == 'O':
#                 candidates.append([i, n-1])
#         
#         print("candidates: ")
#         print(candidates)
#         # DFS candidates to get noFLip[]
#         noFlip = []        
#         for i, j in candidates:
#             if isVisited[i][j]:
#                 continue
#             
#             self.dfs(i, j, isVisited, candidates, board, m, n)
# 
#         # Rescan to flip
#         for i in xrange(1, m-1):
#             for j in xrange(1, n-1):
#                 if board[i][j] == 'O' and [i, j] not in noFlip:
#                     board[i][j] == 'X'
#         
#         return 
#                     
# 
#     def dfs(self, i, j, isVisited, noFlip, board, m, n):
#         if isVisited[i][j]:
#             return
# 
#         noFlip.append([i, j])
#         isVisited[i][j] = True
#         
#         if i+1 < m and not isVisited[i+1][j]:
#             self.dfs(i+1, j, isVisited, noFlip, board, m, n)
#         if i-1 >= 0 and not isVisited[i-1][j]:
#             self.dfs(i-1, j, isVisited, noFlip, board, m, n)
#         if j+1 < n and not isVisited[i][j+1]:
#             self.dfs(i, j+1, isVisited, noFlip, board, m, n)
#         if j-1 >= 0 and not isVisited[i][j-1]:
#             self.dfs(i, j-1, isVisited, noFlip, board, m, n)
# 
