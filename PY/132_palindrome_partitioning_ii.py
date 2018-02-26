# 132. Palindrome Partitioning II  QuestionEditorial Solution  My Submissions
# Total Accepted: 58982
# Total Submissions: 256833
# Difficulty: Hard
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# 2018.02.24
# Use dp[i] to record the mincut for dp[i-1], iniiate to m + 1 each
# for center i, and length j
# If Range[i-j, i+j] is palindrome, then dp[i+j] = min(dp[i+j], dp[i-j-1] + 1) 
# Edge case, if i - j - 1 < 0, which means i-j is the start of the s, so no cut is needed.
# For Range[i-j-1, i+j] is palindrome, update [i+j] = min(dp[i+j], dp[i-j-2] + 1)


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [ n + 1 for x in xrange(n)]
        
        for i in xrange(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                dp[i+j] = min(dp[i+j], dp[i-j-1] + 1) if i-j-1 >= 0 else 0
                j += 1
            j = 0
            while i - j - 1 >= 0 and i + j < n and s[i-j-1] == s[i+j]:
                dp[i+j] = min(dp[i+j], dp[i-j-2] + 1) if i-j-2 >= 0 else 0
                j += 1
        return dp[n-1]



# Better solution. Combine check and update cut at the same time.
# note:
# 1. Initiate dp with [-1, 0, 1, 2 ...]

# 1.1.2017 n length dp
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1: return 0
        dp = [ n + 1 for x in xrange(n) ]

        for i in xrange(n):            # i Center, j center len
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                dp[i+j] = min(dp[i+j], dp[i-j-1] + 1) if i - j - 1 >= 0 else 0
                j += 1
            
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i-j] == s[i+j+1]:
                dp[i + j + 1] = min(dp[i+j+1], dp[i-j-1] + 1) if i - j - 1 >= 0 else 0
                j += 1
            
        return dp[-1]
            

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [ x-1 for x in xrange(n+1)]
        for i in xrange(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:    # odd length
                dp[i+j+1] = min(dp[i+j+1], dp[i-j]+1)
                j += 1

            j = 1
            while i-j+1 >= 0 and i +j < n and s[i-j+1] == s[i+j]: # even
                dp[i+j+1] = min(dp[i+j+1], dp[i-j+1]+1)
                j += 1

        print(dp)
        return dp[-1]
        

# Too slow. Getting TLE 

import sys
class Solution2(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == 1:
            return 0
        n = len(s)
        dp = [ 0 for x in xrange(n)]
        
        for i in xrange(n):
            dp[i] = sys.maxint
            if self.isPalindrome(s[:i+1]):
                dp[i] = 0
                continue
                
            for j in xrange(1, i+1):
                if self.isPalindrome(s[j:i+1]):
                    dp[i] = min(dp[i], dp[j-1] + 1)

        print(dp)
        return dp[-1]
                    
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
            
        return True
        

if __name__  == "__main__":
#    Solution().minCut("ab")
    Solution().minCut("aab")
#    Solution().minCut("aabba")
#    Solution().minCut("aabbaacdc")
#     Solution().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


