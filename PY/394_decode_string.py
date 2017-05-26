# 394. Decode String Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 27861 Total Submissions: 68191 Difficulty: Medium Contributor: LeetCode
# Given an encoded string, return it's decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# 2017.05.22 
# Self wrote. Stack solution
from collections import deque
import string
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        d1, d2 = deque(), deque()
        n = len(s)
        i = 0
        res = ""
        while i < n:
            if s[i] in "0123456789":
                j = i + 1
                while j < n and s[j] in "0123456789":
                    j += 1
                d1.append(int(s[i:j]))
                i = j
                continue
            
            if s[i] == "[": # Read string has []
                j = i + 1
                while j < n and s[j] in string.letters:
                    j += 1
                d2.append(s[i+1:j])
                i = j 
                continue
            
            if s[i] in string.letters:  # string no []
                j = i
                while j < n and s[j] in string.letters:
                    j += 1
                res += s[i:j]
                i = j
                continue
            
            if s[i] == "]":
                j = i + 1
                while j < n and s[j] in string.letters:
                    j += 1
                multi, tmp = d1.pop(), d2.pop()
                if d2:
                    cur = d2.pop() + tmp * multi + s[i+1:j]
                    d2.append(cur)
                else:
                    res += tmp * multi + s[i+1:j]
                i = j
        return res
