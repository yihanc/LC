# 425. Word Squares Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 7392
# Total Submissions: 17526
# Difficulty: Hard
# Contributor: LeetCode
# Given a set of words (without duplicates), find all word squares you can build from them.
# 
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
# 
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
# 
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
# 
# Input:
# ["area","lead","wall","lady","ball"]
# 
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:
# 
# Input:
# ["abat","baba","atan","atal"]
# 
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# 2017.05.22
# Trie + DFS
# Trie saves words for the prefix in the list
class TrieNode(object):
    def __init__(self):
        self.children = [ None for x in xrange(26) ]
        self.wordlist = []

class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            cur = self.root     # Add each word
            for char in word:
                i = ord(char) - 97
                if cur.children[i] == None: cur.children[i] = TrieNode()
                cur.wordlist.append(word)
                cur = cur.children[i]
    
    def searchPrefixes(self, prefix):
        cur = self.root
        for char in prefix:
            i = ord(char) - 97
            if cur.children[i] == None: return []
            cur = cur.children[i]
        return cur.wordlist
        
        
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res = []
        tr = Trie(words)
        n, nw = len(words), len(words[0])
        if n == 0 or nw == 0: return []
        for word in words:
            self.dfs(res, [word], tr, 1, nw)
        return res
    
    def dfs(self, res, line, tr, i, nw):
        if i == nw:
            res.append(line)
            return
        
        prefix = ""
        for word in line:
            prefix += word[i]
        words = tr.searchPrefixes(prefix)
        for word in words:
            self.dfs(res, line + [word], tr, i + 1, nw)
