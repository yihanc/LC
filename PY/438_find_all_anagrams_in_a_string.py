# 438. Find All Anagrams in a String
# DescriptionHintsSubmissionsDiscussSolution
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# 2018.02.25
# Sliding window 
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        key = Counter(p)
        s_counts = Counter(s[:n])
        res = []
        for i in xrange(m - n + 1):
            if i != 0:
                s_counts[s[i-1]] -= 1
                if s_counts[s[i-1]] == 0: del s_counts[s[i-1]]
                s_counts[s[i+n-1]] += 1
            if s_counts == key:
                res.append(i)
        return res
            
            

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        key = Counter(p)
        return [ i for i in xrange(m - n + 1) if Counter(s[i:i+n]) == key ]
