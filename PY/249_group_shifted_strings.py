# 249. Group Shifted Strings Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23516
# Total Submissions: 58148
# Difficulty: Medium
# Contributor: LeetCode
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# 
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
# 
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:
# 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

# 2018.02.24
from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        res = []
        for s in strings:
            if len(s) == 1: 
                dic["a"].append(s)
                continue
            key = self.getKey(s)
            dic[key].append(s)
        return [ v for k, v in dic.iteritems() ]
    
    def getKey(self, s):
        diff = ord(s[0]) - ord('a')
        key = "a"
        for i in xrange(1, len(s)):
            x = ord(s[i]) - diff
            if x < ord('a'): x += 26
            key += chr(x)
        return key


# 2017.05.26
# Similar to anagram
from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def getKey(_s):
            if len(_s) == 1: return 'a'
            distance = ord(_s[0]) - ord('a')
            key = ""
            for char in _s:
                i = ord(char) - distance
                if i < ord('a'): i += 26
                if i > ord('z'): i -= 26
                key += chr(i)
            return key
        
        dic = defaultdict(list)
        for s in strings:
            key = getKey(s)
            dic[key].append(s)
        res = []
        for a, b in dic.iteritems():
            res.append(b)
        return res
    
