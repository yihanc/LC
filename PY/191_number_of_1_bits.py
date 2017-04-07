# 191. Number of 1 Bits Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 141318
# Total Submissions: 363032
# Difficulty: Easy
# Contributor: LeetCode
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1: count += 1
            n >>= 1
        return count
        

