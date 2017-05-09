# 208. Implement Trie (Prefix Tree) Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 67375
# Total Submissions: 254071
# Difficulty: Medium
# Contributors: Admin
# Implement a trie with insert, search, and startsWith methods.
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# Subscribe to see which companies asked this question.

# 2015.05.05 another version of TrieNode implementation
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not p.next[i]: p.next[i] = TrieNode()
            p = p.next[i]
        p.word = word
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not p.next[i]: return False
            p = p.next[i]
        return p.word == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not p.next[i]: return False
            p = p.next[i]
        return True

class TrieNode(object):
    def __init__(self):
        self.next = [ None for x in xrange(26) ]
        self.word = ""

from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isword
                

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
            
