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


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dic = {}
        for char in t:
            dic[char] = 1

        return res
        
        


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))

