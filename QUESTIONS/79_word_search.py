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
        
        print(word[index], board[i][j], i, j)
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

if __name__ == "__main__":
    board = ["ABCE","SFES","ADEE"]
    word = "ABCESEEEFS"
#    board = [
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
    for row in board:
        print(row)
    print(Solution().exist(board, word))
#    print(Solution().exist(board, "ABCCED"))
#    print(Solution().exist(board, "SEE"))
#    print(Solution().exist(board, "ABCB"))
