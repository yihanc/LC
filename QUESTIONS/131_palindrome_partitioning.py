# 131. Palindrome Partitioning  QuestionEditorial Solution  My Submissions
# Total Accepted: 77173
# Total Submissions: 260026
# Difficulty: Medium
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return
# 
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
# Subscribe to see which companies asked this question

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
