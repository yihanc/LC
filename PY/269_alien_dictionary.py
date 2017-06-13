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
# 05.30 some optimization. Remove lines for handling duplicate. use "".join instead string catenation.
from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words: return ""
        
        indegrees = defaultdict(int)
        outdegrees = defaultdict(list)
        
        for word in words:
            for char in word:
                if char not in indegrees:
                    indegrees[char]
                    outdegrees[char]
        
        for i in xrange(1, len(words)):
            w1, w2 = words[i-1], words[i]
            n = min(len(w1), len(w2))
            for j in xrange(n):
                if w1[j] != w2[j]:
                    indegrees[w2[j]] += 1           # No need to handle duplicate. it is just two lines 
                    outdegrees[w1[j]].append(w2[j])
                    break
        
        d = deque()
        for k, v in indegrees.iteritems():
            if v == 0:
                d.appendleft(k)
        
        res = []
        while d:
            cur = d.pop()
            res.append(cur)
            for out in outdegrees[cur]:
                indegrees[out] -= 1
                if indegrees[out] == 0: d.appendleft(out)
        return "".join(res) if len(res) == len(indegrees) else ""
            


        


# Cases
# ["z","z"]
# expect: "z"

# ["za","zb","ca","cb"]
# expected: "abzc"

# ["wnlb"]
# expected: "blnw"
