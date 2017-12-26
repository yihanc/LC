# 179. Update Bits 
# Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N located at i and starting at j)
# 
#  Notice
# In the function, the numbers N and M will given in decimal, you should also return a decimal number.
# 
# Have you met this question in a real interview? Yes
# Clarification
# You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.
# 
# Example
# Given N=(10000000000)2, M=(10101)2, i=2, j=6
# 
# return N=(10001010100)2
# 
# Challenge 
# Minimum number of operations?


class Solution:
    """
    @param: n: An integer
    @param: m: An integer
    @param: i: A bit position
    @param: j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        # write your code here
        # Idea is to mask n[i:j] into 0 and or m
        # N:    0000 0000 0000 0000 0000 0010 0010 0000
        # Mask: 1111 1111 1111 1111 1111 1111 1000 0011
        # Idea is: N & mask | (m << i)
        #
        def _toTwoComplement(bits, value):
            return ((1 << bits) - 1) & value
        
        n_two = _toTwoComplement(32, n)

        ones = int("1" * 32, 2)
        mask_bits = ""
        idx = 0
        while idx <= 31:
            if idx >= i and idx <= j:
                mask_bits = "0" + mask_bits
            else:
                mask_bits = "1" + mask_bits
            idx += 1
            
        mask = int(mask_bits, 2)
        ans = n_two & mask | (m << i)

        return - ((ans ^ ones) + 1) if ans > (2 ** 31 - 1) else ans
