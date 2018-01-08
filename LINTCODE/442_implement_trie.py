class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
        
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        p = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not p.next[i]:
                p.next[i] = TrieNode()
            p = p.next[i]
        p.word = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        p = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not p.next[i]: return False
            p = p.next[i]
        return p.word == word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        p = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if not p.next[i]: return False
            p = p.next[i]
        return True

class TrieNode():
    def __init__(self):
        self.next = [ None ] * 26
        self.word = ""
