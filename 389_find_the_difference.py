# 389. Find the Difference Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 66347
# Total Submissions: 128845
# Difficulty: Easy
# Contributor: LeetCode
# Given two strings s and t which consist of only lowercase letters.
# 
# String t is generated by random shuffling string s and then add one more letter at a random position.
# 
# Find the letter that was added in t.
# 
# Example:
# 
# Input:
# s = "abcd"
# t = "abcde"
# 
# Output:
# e
# 
# Explanation:
# 'e' is the letter that was added.

# 2017.05.20
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for char in t:
            if char not in dic or dic[char] == 0:
                return char
            else:
                dic[char] -= 1
