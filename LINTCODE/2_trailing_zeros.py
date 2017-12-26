# 2. Trailing Zeros 
# Write an algorithm which computes the number of trailing zeros in n factorial.
# 
# Have you met this question in a real interview? Yes
# Example
# 11! = 39916800, so the out should be 2

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators
        res = 0
        i = 5
        while i <= n:
            res += n // i
            i *= 5
        return res
            
