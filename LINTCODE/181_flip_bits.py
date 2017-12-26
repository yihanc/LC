# 181. Flip Bits 
# Determine the number of bits required to flip if you want to convert integer n to integer m.
# 
#  Notice
# Both n and m are 32-bit integers.
# 
# Have you met this question in a real interview? Yes
# Example
# Given n = 31 (11111), m = 14 (01110), return 2.

class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        def toTwoComplement(bits, value):
            return ((1 << bits) - 1) & value
            
        return bin(toTwoComplement(32, a) ^ toTwoComplement(32, b)).count("1")
        

