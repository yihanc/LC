# 395. Longest Substring with At Least K Repeating Characters
# DescriptionHintsSubmissionsDiscussSolution
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
# 


# 2018.02.23 Divide and Conquer
# Two pointer is hard to maintain the state

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max([ self.longestSubstring(x, k) for x in s.split(c) ])
        return len(s)
              