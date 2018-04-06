'''461. Hamming Distance
DescriptionHintsSubmissionsDiscussSolution
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

# 2018.03.10
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(32):
            cnt = cnt + 1 if (x & 1) != (y & 1) else cnt
            x, y = x >> 1, y >> 1
        return cnt
            

