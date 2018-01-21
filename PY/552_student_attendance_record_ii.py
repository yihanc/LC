# 552. Student Attendance Record II
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
# 
# A student attendance record is a string that only contains the following three characters:
# 
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# 
# Example 1:
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times. 
# Note: The value of n won't exceed 100,000.


# res[i] represent the result at i time
# 1. Calculate cases without A. dp[i] represent insert i "P" or "L". dp[n] is the ans
# 2. Then replace A with any position, so for size 0 to n, res += dp[size] * dp[n-1-size]

# 1. Without A cases
# res[i] = Cases ending with "P" + Cases ending with "PL" + Cases ending with "PLL"
# if ending with "P", res[i-1]
# If ending with "PL", res[i-2]
# If ending with "PLL",  res[i-3]
# not "LLL"
# res[i] = res[i-1] + res[i-2] + res[i-3]
# 2. With A cases


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8
        
        TOMOD = 10**9 + 7
        dp = [1, 2, 4]  # i present insert i non-A elements
        for i in xrange(3, n + 1):   # 1st, insert n - 1 element non-A elements
            dp.append(sum(dp[-3:]) % TOMOD)
        res = dp[-1]
        for size in xrange(n):             # i is is the length of left sub. 
            res += (dp[size] * dp[n-size-1]) % TOMOD
            res %= TOMOD
        return res


# Analysis
# Sequential DP
# Use A[i], P[i], L[i] to record the value of i-th char is "A", "P" or "L"
# It is easy to see that:
# P[i] = A[i-1] + P[i-1] + L[i-1]
# L[i] = A[i-1] + P[i-1] + (A[i-2] + L[i-2])  # A[i-2] + L[i-2] is the case that L[i-1] exclude "LL" case

# 1) A[i] = noAP[i-1] + noAL[i-1]  # noAP[i-1] means i-1th char is "P" and no "A" before, 
# 2) For noAP[i] = noAP[i-1] + noAL[i-1]
# 3) For noAL[i] = noAP[i-1] + noAP[i-2] (Can't have noaL[i-2] to exclue "LL")

# Simplify:
# From 1), A[i] = noAP[i]
# From 2), noAL[i] = A[i-1] + A[i-2], 
# Subsitute to 1) right,  A[i] = A[i-1] + A[i-2] + A[i-3]

# DP:
# m/n        i = 0,   1,    2,    3,   4,
# 0, A[]        1     2     4     7
# 1, P[]        1     3     8    19
# 2, L[]        1     3     7     

# TLE for large case. 49 / 58 test cases passed.
# Same C++ code passed
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8
        m = 3
        TOMOD = 10**9 + 7
        dp = [ [ 0 for j in xrange(n)] for i in xrange(m)]
        
        for i in xrange(m):
            dp[i][0] = 1
        
        dp[0][1], dp[1][1], dp[2][1]  = 2,3,3
        dp[0][2] = 4
        
        for j in xrange(2, n):
            if j > 2: dp[0][j] = (dp[0][j-1] + dp[0][j-2] + dp[0][j-3]) % TOMOD
            dp[1][j] = (dp[0][j-1] + dp[1][j-1] + dp[2][j-1]) % TOMOD
            dp[2][j] = (dp[0][j-1] + dp[1][j-1] + dp[0][j-2] + dp[1][j-2]) % TOMOD
            
        #for row in dp:
        #    print row
        return (dp[0][n-1] + dp[1][n-1] + dp[2][n-1]) % TOMOD
