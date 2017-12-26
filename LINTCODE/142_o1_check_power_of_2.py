# 142. O(1) Check Power of 2 
# Using O(1) time to check whether an integer n is a power of 2.
# 
# Have you met this question in a real interview? Yes
# Example
# For n=4, return true;
# For n=5, return false;



class Solution:
    """
    @param: n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n <= 0: return False
        return (n & (n - 1)) == 0
