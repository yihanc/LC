# 459. Repeated Substring Pattern   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 11329
# Total Submissions: 28649
# Difficulty: Easy
# Contributors: YuhanXu
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# 
# Example 1:
#     Input: "abab"
# 
#     Output: True
# 
#     Explanation: It's the substring "ab" twice.
#     Example 2:
#     Input: "aba"
# 
#     Output: False
#     Example 3:
#     Input: "abcabcabcabc"
# 
#     Output: True
# 
#     Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        if n <= 1: return False
        
        for sublen in xrange(1, n // 2 + 1):
            if n % sublen != 0: continue
            substr = str[:sublen]
            start, end = sublen, sublen * 2
            while end < n and substr == str[start:end]:
                start, end = start + sublen, end + sublen
            
            if end == n and substr == str[start:end]:
                return True
        
        return False
