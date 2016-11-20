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
        A = [ 0 ] * 128
        for char in t:
            A[ord(char)] += 1
            
        counter, l, r, min_len, head = len(t), 0, 0, len(s)+1, 0
        while r < len(s):
            if A[ord(s[r])] > 0:
                counter -= 1
            
            A[ord(s[r])] -= 1
            r += 1
            
            while counter == 0:     # Window found
                if r - l < min_len: 
                    head = l        # update head
                    min_len = r - head
                
                A[ord(s[l])] += 1   # When to update l
                if A[ord(s[l])] > 0:
                    counter += 1
                l += 1
        
        if min_len == len(s) + 1:   # No window found
            return ""
        else:
            return s[head: head+min_len]
        


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))