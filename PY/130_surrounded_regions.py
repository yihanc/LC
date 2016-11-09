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

class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
    

if __name__ == "__main__":
    board = ["XXXX","XOOX","XXOX","XOXX"]
    Solution().solve(board)

### DFS maximum recursion depth exceeded
# See if '0' is attached to edge.
class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: 
            return
        
        m, n = len(board), len(board[0])    #Special cases, if m or n <= 2. return all XXX
        candidates = []                      #i, j
        isVisited = [[ False for j in xrange(n)] for i in xrange(m)]

        # Scan all sides and get candidates
        for j in xrange(n):
            if board[0][j] == 'O':
                candidates.append([0, j])
            if m == 1:
                break
            if board[m-1][j] == 'O':
                candidates.append([m-1, j])
        
        for i in xrange(m):
            if board[i][0] == 'O':
                candidates.append([i, 0])
            if n == 1:
                break
            if board[i][n-1] == 'O':
                candidates.append([i, n-1])
        
        print("candidates: ")
        print(candidates)
        # DFS candidates to get noFLip[]
        noFlip = []        
        for i, j in candidates:
            if isVisited[i][j]:
                continue
            
            self.dfs(i, j, isVisited, candidates, board, m, n)

        # Rescan to flip
        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if board[i][j] == 'O' and [i, j] not in noFlip:
                    board[i][j] == 'X'
        
        return 
                    

    def dfs(self, i, j, isVisited, noFlip, board, m, n):
        if isVisited[i][j]:
            return

        noFlip.append([i, j])
        isVisited[i][j] = True
        
        if i+1 < m and not isVisited[i+1][j]:
            self.dfs(i+1, j, isVisited, noFlip, board, m, n)
        if i-1 >= 0 and not isVisited[i-1][j]:
            self.dfs(i-1, j, isVisited, noFlip, board, m, n)
        if j+1 < n and not isVisited[i][j+1]:
            self.dfs(i, j+1, isVisited, noFlip, board, m, n)
        if j-1 >= 0 and not isVisited[i][j-1]:
            self.dfs(i, j-1, isVisited, noFlip, board, m, n)

