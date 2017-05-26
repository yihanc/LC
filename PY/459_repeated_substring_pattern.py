# 459. Repeated Substring Pattern Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 28053
# Total Submissions: 73141
# Difficulty: Easy
# Contributors:
# YuhanXu
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# 
# Example 1:
# Input: "abab"
# 
# Output: True
# 
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
# 
# Output: False
# Example 3:
# Input: "abcabcabcabc"
# 
# Output: True
# 
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


# 2017.05.24
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for size in xrange(1, n // 2 + 1):
            if n % size != 0: continue
            i = 0
            while (i + 2 * size) <= n and s[i:(i+size)] == s[(i+size):(i+2*size)]:
                i = i + size
            if i + size == n: return True
        return False
                
