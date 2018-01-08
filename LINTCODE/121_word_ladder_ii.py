



# Simple BFS but TLE for large case

import string
from collections import deque, defaultdict

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        if start in dict: dict.remove(start)
        if end in dict: dict.remove(end)
        
        routes = defaultdict(set)
        d = deque()
        
        d.append([1, start])
        dep_ans = None
        words_to_delete = set()
        
        while d:
            dep, word = d.pop()
            #print(dep, word, d)
            if dep_ans and dep > dep_ans: break
            
            for i in xrange(len(word)):
                for char in string.lowercase:
                    new_word = word[:i] + char + word[i+1:]
                    
                    if new_word == end:
                        #print(word, new_word)
                        routes[end].add(word)
                        dep_ans = dep
                        break
                
                    if new_word in dict:
                        #print(word, new_word)
                        routes[new_word].add(word)
                        d.appendleft([dep + 1, new_word])
                        words_to_delete.add(new_word)
                

            if not d or dep < d[-1][0]:
                for word in words_to_delete:
                    dict.remove(word)
                words_to_delete = set()
                
        #print(routes)        
        res = [[end]]
        while res[0][0] in routes:
            tmp = res
            res = []
            for line in tmp:
                for next_word in routes[line[0]]:
                    res.append([next_word] + line)
        #print(res)
        return res
        
        
