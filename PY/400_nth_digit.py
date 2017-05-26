# 400. Nth Digit Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 20423
# Total Submissions: 67770
# Difficulty: Easy
# Contributor: LeetCode
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

# 2017.05.21
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 9
        size = 1
        start = 1
        
        while n > size * count:
            n -= size * count
            size += 1
            count *= 10
            start *= 10
        
        start = start + (n - 1) // size
        return int(str(start)[(n - 1) % size])
