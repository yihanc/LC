# 212. Word Search II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 41990
# Total Submissions: 183699
# Difficulty: Hard
# Contributor: LeetCode
# Given a 2D board and a list of words from the dictionary, find all words in the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# 
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
# 
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# click to show hint.
# 
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# 
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.


# 2018.01.11 BackTracking + Trie
from collections import deque
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        tr = Trie()
        for word in words:
            tr.insert(word)

        res = []
        for i in xrange(m):
            for j in xrange(n):
                char = board[i][j]
                index = ord(char) - ord('a')
                if tr.root.children[index]:
                    board[i][j] = "#"
                    self.helper(board, tr.root.children[index], res, char, i, j)
                    board[i][j] = char 
        return res
    
    def helper(self, board, node, res, line, i, j):
        if node.word == line:
            res.append(line)
            node.word = ""

        m, n = len(board), len(board[0])
        pairs = [[0, 1], [0,-1], [1,0],[-1,0]]
        for pair in pairs:
            ii, jj = i + pair[0], j + pair[1]
            if ii < 0 or ii >= m or jj < 0 or jj >= n or board[ii][jj] == "#":
                continue

            char = board[ii][jj]
            index = ord(char) - ord('a')
            if not node.children[index]:
                continue
                
            board[ii][jj] = "#"
            self.helper(board, node.children[index], res, line + char, ii, jj)
            board[ii][jj] = char
        
        
class TrieNode(object):
    def __init__(self):
        self.children = [ None for x in xrange(26) ]
        self.word = ""
        
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not node.children[i]:    # BIG Bug if forgetting this line
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = word


        

# 2017.05.04
# Build Trie from words. 
# DFS boards and compare with words

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words: return []
        res = []
        root = self.buildTrie(words)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res
    
    def dfs(self, board, i, j, p, res):
        c = board[i][j]
        if c == '#' or not p.next[ord(c) - ord('a')]: return
        p = p.next[ord(c) - ord('a')]
        if p.word:
            res.append(p.word)
            p.word = ""   # de-dupliacte
        
        board[i][j] = '#'
        if i > 0: self.dfs(board, i - 1, j, p, res)
        if j > 0: self.dfs(board, i, j - 1, p, res)
        if i < len(board) - 1: self.dfs(board, i + 1, j, p, res)
        if j < len(board[0]) - 1: self.dfs(board, i, j + 1, p, res)
        board[i][j] = c

    def buildTrie(self, words):
        root = TrieNode()
        for w in words:
            p = root
            for c in w:
                i = ord(c) - ord('a')
                if not p.next[i]: p.next[i] = TrieNode()
                p = p.next[i]
            p.word = w
        return root
        
class TrieNode(object):
    def __init__(self):
        self.next = [ None for x in xrange(26)]
        self.word = ""

