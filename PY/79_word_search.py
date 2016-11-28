# 79. Word Search   QuestionEditorial Solution  My Submissions
# Total Accepted: 97542
# Total Submissions: 393048
# Difficulty: Medium
# Contributors: Admin
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# 11.27.2016 Backtracking + candidates
class Solution(object):
    found = False
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nword = len(word)
        if nword == 0: return False
        
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '.'
                    self.dfs(board, word, i, j, 1, m, n)
                    board[i][j] = tmp
                    if self.found:
                        return True
                        
        return False
            
    def dfs(self, board, word, i, j, index, m, n):
        if len(word) == index:
            self.found = True
            return
        
        candidates = []
        
        if i - 1 >= 0 and word[index] == board[i-1][j]:
            candidates.append([i-1, j])
        if j - 1 >= 0 and word[index] == board[i][j-1]:
            candidates.append([i, j-1])
        if i + 1 < m and word[index] == board[i+1][j]:
            candidates.append([i+1, j])
        if j + 1 < n and word[index] == board[i][j+1]:
            candidates.append([i, j+1])
            
        for x, y in candidates:
            tmp = board[x][y]
            board[x][y] = '.'
            self.dfs(board, word, x, y, index+1, m, n)
            if self.found: 
                return 
            board[x][y] = tmp
            
        
        

class Solution2(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: 
            return True

        if not board or len(board) * len(board[0]) < len(word):
            return False

        return self.dfs(board, word, 0, 0, 0, False)
        
    def dfs(self, board, word, i, lastI, lastJ, res):
        print(i)
        if res or i == len(word):
            return True
        
        m, n = len(board), len(board[0])

        if i == 0:  # search entire board
            for x in xrange(m):
                for y in xrange(n):
                    if board[x][y] == word[0]:
                        board[x][y] = ""
                        if self.dfs(board, word, i+1, x, y, False):
                            return True
                        board[x][y] = word[0]
        else:       # search lastI+1, lastI-1, lastJ+1,lastJ-1
            candidates = []
            if lastI+1 < m and board[lastI+1][lastJ] == word[i]:
                candidates.append([lastI+1, lastJ])
            if lastI-1 >= 0 and board[lastI-1][lastJ] == word[i]:
                candidates.append([lastI-1, lastJ])
            if lastJ+1 < n and board[lastI][lastJ+1] == word[i]:
                candidates.append([lastI, lastJ+1])
            if lastJ-1 >= 0 and board[lastI][lastJ-1] == word[i]:
                candidates.append([lastI, lastJ-1])

            for x, y in candidates:
                board[x][y] = ""
                if self.dfs(board, word, i+1, x, y, False):
                    return True
                board[x][y] = word[i]

        return False
                

if __name__ == "__main__":
    board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
    for row in board:
        print(row)
#    print(Solution().exist(board, "ABCCED"))
#    print(Solution().exist(board, "SEE"))
    print(Solution().exist(board, "ABCB"))
