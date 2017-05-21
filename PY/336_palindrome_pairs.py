# 336. Palindrome Pairs Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23249
# Total Submissions: 90734
# Difficulty: Hard
# Contributor: LeetCode
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
# 
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
# 

# 2017.05.18
# Map + prefix
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words) <= 1: return []
        n = len(words)
        res = []
        dic = {}
        for i in xrange(n): dic[words[i]] = i
        #print(dic)
        for i in xrange(n):
            for j in xrange(len(words[i]) + 1):
                str1 = words[i][:j]
                str2 = words[i][j:]
                #print(str1, str2)
                if self.isPalindrome(str1):
                    str2rev = str2[::-1]
                    if str2rev in dic and i != dic[str2rev]:
                        res.append([dic[str2rev], i])
                if str2 and self.isPalindrome(str2):    # str2 != "" to avoid duplicate
                    str1rev = str1[::-1]
                    if str1rev in dic and i != dic[str1rev]:
                        #print(str1rev, dic[str1rev])
                        res.append([i, dic[str1rev]])
        return res
    
    def isPalindrome(self, s):
        if not s: return True
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l, r = l + 1, r - 1
        return l >= r


# 2017.05.18
# Naive Solution  Time complexity loop n^2, isPalidrome, 2 * wordlength * 2 (best o(1), worst o(word length + length))
# Total n ^2 * avg * len(word)
# How to optimize? for each word, put all its possible in map
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = []
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if self.isPalindrome(words[i] + words[j]):
                    res.append([i, j])
                if self.isPalindrome(words[j] + words[i]):
                    res.append([j, i])
        return res
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l, r = l + 1, r - 1
        return l >= r
