# 326. Power of Three
# Description  Submission  Solutions  Add to List
# Total Accepted: 82356
# Total Submissions: 208710
# Difficulty: Easy
# Contributors: Admin
# Given an integer, write a function to determine if it is a power of three.
# 
# Follow up:
# Could you do it without using any loop / recursion?
# 
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        start = 1
        while start < n:
            start = start * 3
        
        return start == n
