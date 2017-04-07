# 5. Longest Palindromic Substring   My Submissions QuestionEditorial Solution
# Total Accepted: 108992 Total Submissions: 469979 Difficulty: Medium
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# 2017.04.07
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        res = ""
        while i < len(s):
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i+j] == s[i-j]:
                j += 1
            if 2 * j - 1 > len(res): res = s[i-j+1:i+j]
        
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i-j] == s[i+j+1]:
                j += 1
            if 2 * j > len(res): res = s[i-j+1:i+j+1]
            i += 1
        return res


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #1 Preprocess
        new_s = "^#" + "#".join(list(s)) + "#$"
        
        #2 Process
        P = [0 for x in new_s]
        
        center, right = 0, 0
        i = 1
        while i < len(new_s) - 1:
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            while new_s[i + P[i] + 1] == new_s[i - P[i] -1]:
                P[i] += 1
            if i + P[i] > right:
                right = i + P[i]
                center = i
            i += 1
            
        #3 Get result
        mx = max(P)
        center = P.index(mx)
        return new_s[center - mx: center + mx + 1].replace("#", "")
