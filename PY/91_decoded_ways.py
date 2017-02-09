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

# 12.30.2016 Rewrite. n size dp[]
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        
        dp = [ 0 for j in xrange(n) ]

        for i in xrange(n):
            if s[i] in "123456789":
                dp[i] = dp[i-1] if i > 0 else 1
            
            if i > 0 and ( s[i-1] == "0" or int(s[i-1:i+1]) >= 27 ):
                continue
            
            if i > 0 and int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i] + dp[i-2] if i >= 2 else dp[i] + 1
        
        return dp[-1]

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

# 12.1.2016 Rewrite. n + 1 size dp[]
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [ 0 for x in xrange(n+1) ]
        dp[0] = 1   # For "" case
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

        return dp[-1]

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
    
