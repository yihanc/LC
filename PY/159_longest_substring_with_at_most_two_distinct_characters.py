# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# 
# For example, Given s = “eceba” and k = 2,
# 
# T is "ece" which its length is 3.

# 2017.05.27
# dic + l r window
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res, l, r = 0, 0, 0
        while r <= len(s):
            res = max(res, r - l)
            if r == len(s): break
            if len(dic) == 2 and s[r] not in dic:   # move left
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
                continue
            
            if r < len(s):
                dic[s[r]] = dic.get(s[r], 0) + 1
            r += 1
        return res
        
