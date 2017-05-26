# 340. Longest Substring with At Most K Distinct Characters Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 20917
# Total Submissions: 54455
# Difficulty: Hard
# Contributor: LeetCode
# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# 
# For example, Given s = “eceba” and k = 2,
# 
# T is "ece" which its length is 3.

# 2017.05.21
# Self-wrote
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0: return 0
        if len(s) < k: return len(s)
        res = 0
        dic = {}
        
        l, r = 0, 0
        while r < len(s):
            res = max(res, r - l)
            if len(dic) == k and s[r] not in dic:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
                continue
                
            dic[s[r]] = dic.get(s[r], 0) + 1
            r += 1
        return max(res, r - l)
