# 76. Minimum Window Substring   QuestionEditorial Solution  My Submissions
# Total Accepted: 79051
# Total Submissions: 340398
# Difficulty: Hard
# Contributors: Admin
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# 
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# 
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
# 
# Subscribe to see which companies asked this question

# Substring Problem Template
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m, n, res, min_l = len(s), len(t), "", 0
        if m == 0 or n == 0: return ""

        tdic = {}
        for char in t:
            if char not in t: t[char] = 1
            else: t[char] += 1

        l, r = 0, 0
        while r < m:
            seen = { c : 0 for char in t }
            
            r += 1
        return
        


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
