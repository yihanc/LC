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

# 2018.11.23 Editor's Solution
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None
        
        while r < len(s):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            
            if c in dict_t and window_counts[c] == dict_t[c]:
                formed += 1
                
            while l <= r and formed == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[c] -= 1
                if c in dict_t and window_counts[c] < dict_t[c]:
                    formed -= 1
                
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# 2018.02.23 Minimum Window Substring
# Use dic and cnt to maintain states
# s[l:r] = Window
# For Each Loop :
# 1) First check if cnt == len(t), if yes, maintain state of s[l] and r += 1
# 2) if not, maintain state of s[r] and l += 1


from collections import Counter, defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        dic = Counter(t)
        
        res = s + "."
        cnt, l, r = 0, 0, 0
        while r <= len(s):
            if cnt == len(t):
                res = s[l:r] if r - l < len(res) else res
                if s[l] in dic:
                    if dic[s[l]] >= 0: cnt -= 1
                    dic[s[l]] += 1
                l += 1
                continue
            
            if r < len(s):
                if s[r] in dic:
                    if dic[s[r]] > 0: cnt += 1
                    dic[s[r]] -= 1
            r += 1
        return res if len(res) < len(s) + 1 else ""
                    
        
        

# 03.04.2016 Self write.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        dic = {}
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        #print(dic)
        n = len(s)
        l, r, count = 0, 0, 0
        res = s + " "
        while r <= n:
            if r == n and count < len(dic): break   #Newly added to optimize
            if count == len(dic):
                #print(l, r, s[l:r], count)
                if r - l < len(res):
                    res = s[l:r]
            
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] == 1: # dic[xx] 0 -> TARGET, count -=1 
                        count -= 1
                l += 1
                continue
            
            if r < n and s[r] in dic:
                dic[s[r]] -= 1
                if dic[s[r]] == 0:  # dic[xx] TARGET -> 0, count += 1
                    count += 1
            r += 1
            
        return res if res != s + " " else ""
            

# 12.30.2016 Rewrite Template
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
            if s[r] in dic:
                if dic[s[r]] > 0: counter -= 1
                dic[s[r]] -= 1
            r += 1
            
            while l < m and counter == 0:
                if r - l < len(res):
                    res = s[l:r]
                
                if s[l] in dic:
                    if dic[s[l]] == 0: counter += 1
                    dic[s[l]] += 1
                l += 1
        
        return "" if len(res) == m + 1 else res


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""

        m, n = len(s), len(t)
        if m < n: return ""
        l, r = 0, 0
        count = n
        
        dic = {}
        for char in t:
            dic[char] = 1
        
        res = s + "."
        while r < m:
            if s[r] in dic and dic[s[r]] > 0:
                dic[s[r]] -= 1
                count -= 1
            r += 1

            print(count, s[r], dic)
            while count == 0:
                print("res: ", s[l:r])
                if len(res) > len(s[l:r]):
                    res = min(res, s[l:r])
                
                if s[l] in dic:
                    if dic[s[l]] == 0:
                        count += 1
                    dic[s[l]] += 1
                l += 1

        return "" if res == (s + ".") else res



if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(s, t)
    print(Solution().minWindow(s, t))

# Substring Problem Template
# class Solution2(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         A = [ 0 ] * 128
#         for char in t:
#             A[ord(char)] += 1
#             
#         counter, l, r, min_len, head = len(t), 0, 0, len(s)+1, 0
#         while r < len(s):
#             if A[ord(s[r])] > 0:
#                 counter -= 1
#             
#             A[ord(s[r])] -= 1
#             r += 1
#             
#             while counter == 0:     # Window found
#                 if r - l < min_len: 
#                     head = l        # update head
#                     min_len = r - head
#                 
#                 A[ord(s[l])] += 1   # When to update l
#                 if A[ord(s[l])] > 0:
#                     counter += 1
#                 l += 1
#         
#         if min_len == len(s) + 1:   # No window found
#             return ""
#         else:
#             return s[head: head+min_len]
#         
