# 266. Palindrome Permutation Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 29995
# Total Submissions: 53248
# Difficulty: Easy
# Contributor: LeetCode
# Given a string, determine if a permutation of the string could form a palindrome.
# 
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.


# 2017.05.23
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1: return True
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        odd = 0
        for k, v in dic.iteritems():
            if v % 2 == 0: continue
            if v % 2 == 1:
                odd += 1
                if odd > 1: return False
        return True
            
            
