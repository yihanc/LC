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

# Careful corner cases:
# "", return 0
# "0", return 0
# "00", return 0
# "100", return 0

# Several cases:
# Empty s or "0", return 0
# in [ "00", "30", "40", "50", "60", "70", "80", "90" ], return 0
# int(tmp) in 11 ~ 19, 21 ~ 26, dp[i+1] = dp[i] + dp[i-1]
# in [ "10", "20" ], dp[i+1] = dp[i-1]
# else, dp[i+1] = dp[i]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if not s or s[0] == "0":
            return 0

        dp = [1 for x in xrange(n+1)]

        # i is the index of string
        for i in xrange(1, n):
            tmp = s[i-1:i+1]
            if tmp in [ "00", "30", "40", "50", "60", "70", "80", "90" ]:
                return 0
            
            if (( int(tmp) >= 11 and int(tmp) <= 19 ) or
                ( int(tmp) >= 21 and int(tmp) <= 26 )):
                dp[i+1] = dp[i] + dp[i-1]
            elif tmp in [ "10", "20" ]:
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[-1]

if __name__ == "__main__":
    Solution().numDecodings("")
    Solution().numDecodings("0")
    Solution().numDecodings("00")
    Solution().numDecodings("100")
    Solution().numDecodings("1")
    Solution().numDecodings("10")
    Solution().numDecodings("12")
    Solution().numDecodings("123")
    Solution().numDecodings("12321")
    
