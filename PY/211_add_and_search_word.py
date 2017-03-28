# 211. Add and Search Word - Data structure design Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 47545
# Total Submissions: 226229
# Difficulty: Medium
# Contributors: Admin
# Design a data structure that supports the following two operations:
# 
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
# 
# For example:
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

# 2017.03.14 Similar to implement Trie. 
# When searching, Use BFS
#

from collections import deque, defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        d = deque()
        d.append([self.root, 0])
        n = len(word)
        
        while d:
            cur, i = d.pop()
            
            if i == n and cur.isword:
                return True
            
            if i == n or word[i] != "." and word[i] not in cur.children:
                continue
            
            if word[i] == ".":
                for k, v in cur.children.iteritems():
                    d.appendleft([v, i + 1])
            elif word[i] in cur.children:
                d.appendleft([cur.children[word[i]], i + 1])
            
        return False
            
            
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
