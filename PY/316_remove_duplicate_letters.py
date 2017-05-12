# 316. Remove Duplicate Letters Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 28480
# Total Submissions: 97932
# Difficulty: Hard
# Contributor: LeetCode
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
# 
# Example:
# Given "bcabc"
# Return "abc"
# 
# Given "cbacdcbc"
# Return "acdb"

#  Recursive o(26n) solution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        cnt = {}
        for char in s:
            cnt[char] = cnt.get(char, 0) + 1
        pos = 0
        for i, x in enumerate(s):
            if x < s[pos]: pos = i
            cnt[x] -= 1
            if cnt[x] == 0: break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))
