# 140. Fast Power 
# Calculate the an % b where a, b and n are all 32bit integers.
# 
# Have you met this question in a real interview? Yes
# Example
# For 231 % 3 = 2
# 
# For 1001000 % 1000 = 0
# 
# Challenge 
# O(logn)


class Solution:
    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """
    #n ** 2 % b == (n %b * n % b ) % b
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        product = self.fastPower(a, b, n / 2)
        res = product ** 2 % b

        if n % 2 == 1:
            res = res * a % b
        return res
        
