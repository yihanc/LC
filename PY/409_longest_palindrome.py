# 409. Longest Palindrome Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 37657
# Total Submissions: 83252
# Difficulty: Easy
# Contributor: LeetCode
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# Example:
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# 2017.05.23
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        res, odd = 0, 0
        print(dic)
        for k, v in dic.iteritems():
            if v % 2 == 1: 
                odd = 1
                res += v - 1
            else:
                res += v
        return res if odd == 0 else res + 1
