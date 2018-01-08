from collections import deque
import string

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end: return 1
        if start in dict: dict.remove(start)
        if end in dict: dict.remove(end)
        
        res = 1
        d = deque()
        d.append([1, start])
        
        while d:
            dep, word = d.pop()
            
            for i in xrange(len(word)):
                for char in string.lowercase:
                    new_word = word[:i] + char + word[i+1:]
                    
                    if new_word == end:
                        return dep + 1
                    
                    if new_word in dict:
                        d.appendleft([dep + 1, new_word])
                        dict.remove(new_word)
        return 0

