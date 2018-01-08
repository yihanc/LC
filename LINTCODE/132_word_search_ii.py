class Solution:
    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words: return []
        m, n = len(board), len(board[0])
        
        tr = Trie(words).root
        res = []
        #print(tr.next)
        for i in xrange(m):
            for j in xrange(n):
                self.dfs(res, "", board, i, j, tr)
        return res

    def dfs(self, res, line, board, i, j, p):
        m, n = len(board), len(board[0])
        index = ord(board[i][j]) - ord('a')
        if board[i][j] == "#" or not p.next[index]: return

        char = board[i][j]
        cur = p.next[index]

        if cur.word == line + board[i][j]:
            res.append(cur.word)
            cur.word = ""                   # Bug 1 
        
        board[i][j] = "#"                       # Bug 2
        pairs = ((0,1), (0,-1), (1,0), (-1,0))
        for (x, y) in pairs:
            ii, jj = i + x, j + y
            if ii < 0 or jj < 0 or ii >= m or jj >= n:
                continue
            self.dfs(res, line + char, board, ii, jj, cur)      # Bug 3, line + char not line + board[i][j]
        board[i][j] = char
        

class Trie():
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    
    def insert(self, word):
        p = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not p.next[i]:
                p.next[i] = TrieNode()
            p = p.next[i]
        p.word = word
        
        
class TrieNode():
    def __init__(self):
        self.next = [None for i in xrange(26)]
        self.word = ""
    
