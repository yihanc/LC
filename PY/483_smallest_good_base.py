# 483. Smallest Good Base
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.
# 
# Now given a string representing n, you should return the smallest good base of n in string format. 
# 
# Example 1:
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
# Example 2:
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
# Example 3:
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# Note:
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading zeros.

# Analysis
#  n = k^m + k^(m-1) ... + k + 1  (1)
# =>  n - 1 = k^m + k^(m-1) ... + k  (2)
# Also  n - k^m = k^(m-1) ... + k + 1 (3)
# From 2 and 3, => n - 1 = k(n - k^m)
# => k^(m+1) - 1 = k*n - n  => n = (k^(m+1) - 1 ) / (k - 1)  (4)
# From binomial thorem,    n > k^m  and n < (k+1)^m
# => so k + 1 > m-th root of n > k

# m is the exponential
# k is base
import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        int(n)
        max_m = int(math.log(n,2))  # Floor func to get the max of m. 
        print("n, max_m", n, max_m)
        for m in xrange(max_m, 1, -1):  #min is 2
            k = int(n**(m**-1))     # formula to calculate base k
            print("---", m, k, (k**(m+1) - 1)//(k-1) )
            if (k**(m+1) - 1)//(k-1) == n:
                return str(k)
        return str(n-1)

# print(Solution().smallestGoodBase(13))
# print(Solution().smallestGoodBase(1000000000000000000))
print(Solution().smallestGoodBase(4681))
