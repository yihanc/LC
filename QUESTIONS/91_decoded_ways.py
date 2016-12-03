# 91. Decode Ways  QuestionEditorial Solution  My Submissions
# Total Accepted: 86240
# Total Submissions: 471037
# Difficulty: Medium
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# 
# The number of ways decoding "12" is 2.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [ 0 for x in xrange(n+1) ]
        dp[0] = 1 
        if n >= 1:
            if s[0] == "0":
                dp[1] = 0
            else:
                dp[1] = 1

        for i in xrange(2, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if s[i-2] == "1" or ( s[i-2] == "2" and s[i-1] in "0123456" ):
                dp[i] += dp[i-2]

        print(s, dp)
        return dp[-1]
        

if __name__ == "__main__":
    print(Solution().numDecodings("27"))
    print(Solution().numDecodings("26"))
    print(Solution().numDecodings("260"))
    print(Solution().numDecodings("2601"))
    print(Solution().numDecodings("2610"))
