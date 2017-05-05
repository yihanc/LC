# 3. Longest Substring Without Repeating Characters   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 222713
# Total Submissions: 944997
# Difficulty: Medium
# Contributors: Admin
# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Subscribe to see which companies asked this question
# 
# 
# # Algorithm
# # window: l, r = 0, 0
# # dic[char] = index.
# # in dic: move l = index +1
# # not in dic: move r, dic[r] = 0
# # update res

# 2017.04.08
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        l, r, n = 0, 0, len(s)
        while r < n:
            if s[r] in dic:
                del dic[s[l]]
                l += 1    
            else:    
                dic[s[r]] = 1
                r += 1
            res = max(res, r - l)
        return res

# 12.11.2016 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        n = len(s)
        res = 0
        l, r = 0, 0
        
        while r < n:
            if s[r] in dic:
                index = dic[s[r]]
                while l != index + 1:
                    del dic[s[l]]
                    l += 1
            dic[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res
                
            
        
