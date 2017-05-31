# 269. Alien Dictionary Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 24166
# Total Submissions: 104804
# Difficulty: Hard
# Contributor: LeetCode
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
# 
# Example 1:
# Given the following words in dictionary,
# 
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
# 
# Example 2:
# Given the following words in dictionary,
# 
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
# 
# Example 3:
# Given the following words in dictionary,
# 
# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".
# 
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.


# 2017.05.27
# topologic sort

from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # idea. scan and build DAG then topological sort
        if len(words) == 0: return ""
        
        ins = defaultdict(int)
        outs = defaultdict(list)
        
        for word in words:
            for char in word:
                ins[char]; outs[char]
        
        for i in xrange(1, len(words)):
            n = min(len(words[i]), len(words[i-1]))
            for j in xrange(n):
                c1, c2 = words[i-1][j], words[i][j]
                if c1 == c2: continue     # If same char, skip.
                if c2 in outs[c1]: break    # if already in map. no update and break
                outs[c1].append(c2)
                ins[c2] += 1
                break
        
        d = deque()
        for k, v in ins.iteritems():
            if v == 0: 
                d.appendleft(k)
                
        res = ""        
        while d:
            char = d.pop()
            res += char
            for nextchar in outs[char]:
                ins[nextchar] -= 1
                if ins[nextchar] == 0:
                    d.appendleft(nextchar)
        return res if len(res) == len(ins) else ""
        
        


# Cases
# ["z","z"]
# expect: "z"

# ["za","zb","ca","cb"]
# expected: "abzc"

# ["wnlb"]
# expected: "blnw"
