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

# 2018.04.08
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        if not word: return True
        m, n = len(board), len(board[0])
        res = [False]
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    self.dfs(board, i, j, word, 0, set(), res)
                    if res[0]: return True
        return res[0]
    
    def dfs(self, board, x, y, word, word_i, vis, res):
        if word_i >= len(word) or board[x][y] != word[word_i]: 
            return
        
        if word_i == len(word) - 1:
            res[0] = True
            return

        vis.add((x, y))
        m, n = len(board), len(board[0])
        pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for pair in pairs:
            xx, yy = x + pair[0], y + pair[1]
            if xx >= 0 and xx < m and yy >= 0 and yy < n and (xx, yy) not in vis:
                self.dfs(board, xx, yy, word, word_i + 1, vis, res)
                if res[0]: return
        vis.remove((x, y))


# 12.28.2016 Rewrite

class Solution(object):
    found = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if not board: return False
        m, n, nw = len(board), len(board[0]), len(word)
        if m * n < nw: return False
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0] and nw == 1:
                    return True
                if board[i][j] == word[0] and nw > 1:
                    isVisited = [ [ False for y in xrange(n) ] for x in xrange(m) ]
                    self.dfs(board, word, 1, i, j, isVisited)
                    if self.found:
                        return True
        return False
                    
    def dfs(self, board, word, index, i, j, isVisited):
        if index == len(word):
            self.found = True
            return
        
        m, n = len(board), len(board[0])
        isVisited[i][j] = True
        
        candidates = []
        if i + 1 < m and not isVisited[i+1][j] and board[i+1][j] == word[index]:
            candidates.append([i + 1, j])
        if j + 1 < n and not isVisited[i][j+1] and board[i][j+1] == word[index]:
            candidates.append([i, j + 1])
        if i - 1 >= 0 and not isVisited[i-1][j] and board[i-1][j] == word[index]:
            candidates.append([i - 1, j])
        if j - 1 >= 0 and not isVisited[i][j-1] and board[i][j-1] == word[index]:
            candidates.append([i, j - 1])        

        for candidate in candidates:
            self.dfs(board, word, index + 1, candidate[0], candidate[1], isVisited)
            if self.found:
                return
        
        isVisited[i][j] = False
        
        

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
