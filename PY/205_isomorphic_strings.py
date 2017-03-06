# 205. Isomorphic Strings Add to List
# Description  Submission  Solutions
# Total Accepted: 93547
# Total Submissions: 285013
# Difficulty: Easy
# Contributors: Admin
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.

# 2017.03.04 Two dics
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        n = len(s)
        
        for i in xrange(n):
            if ((s[i] in dic1 and dic1[s[i]] != t[i])
                or (t[i] in dic2 and dic2[t[i]] != s[i])):
                return False
            else:
                dic1[s[i]] = t[i]
                dic2[t[i]] = s[i]
        return True


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = [ -1 for x in xrange(256) ]
        dic2 = [ -1 for x in xrange(256) ]
        
        for i in xrange(len(s)):
            i1, i2 = ord(s[i]), ord(t[i])
            if dic1[i1] != dic2[i2]: return False
            dic1[i1] = dic2[i2] = i
        
        return True
