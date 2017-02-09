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
            print("i ", i)
            j = 0
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                dp[i+j] = min(dp[i+j], dp[i-j-1] + 1) if i - j - 1 >= 0 else 0
                print("1 ", i, j, s[i-j], s[i+j], dp)
                j += 1
            
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j-1] + 1) if i - j - 1 >= 0 else 0
                print("2 ", i, j, s[i-j], s[i+j+1], dp)
                j += 1
            
        return dp[-1]

if __name__ == "__main__":
    s = "aab"
    print(s)
    print(Solution().minCut(s))
