class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = TrieNode()
        
        
    def addWord(self, word):
        # write your code here
        p = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not p.next[i]:
                p.next[i] = TrieNode()
            p = p.next[i]
        p.word = word
        print (p.word)
        

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.dfs(word, 0, self.root)
        
    
    def dfs(self, word, i, tr):
        print(i, tr.word)
        if i == len(word): return True if tr.word else False
        char = word[i]
        index = ord(char) - ord('a')
        
        if char == ".":
            for next in tr.next:
                if next and self.dfs(word, i + 1, next):
                    return True
        elif tr.next[index]:
            return self.dfs(word, i + 1, tr.next[index])
        
        return False

class TrieNode():
    def __init__(self):
        self.next = [ None ] * 26
        self.word = ""
