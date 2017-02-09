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
        m, n = len(s), len(t)
        dic = {}
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        
        res, l, r, counter = s + ".", 0, 0, n
        while r < m:
            print(l, r, counter, dic)
#            if s[r] in dic and dic[s[r]] > 0:
#                dic[s[r]], counter = dic[s[r]] - 1, counter - 1
            if s[r] in dic:
                if dic[s[r]] > 0: counter -= 1
                dic[s[r]] -= 1
            r += 1
            
            while l < m and counter == 0:
                print("INSIDE", l, r, counter, dic)
                if r - l < len(res):
                    res = s[l:r]
                
#                if s[l] in dic and dic[s[l]] == 0:
#                    dic[s[l]], counter = dic[s[l]] + 1, counter + 1
                if s[l] in dic: 
                    if dic[s[l]] == 0: counter += 1
                    dic[s[l]] += 1
                l += 1
        
        if len(res) == m + 1: 
            return ""
        else: 
            return res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(s, t)
    print(Solution().minWindow(s, t))

