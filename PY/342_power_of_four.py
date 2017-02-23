# 342. Power of Four
# Description  Submission  Solutions  Add to List
# Total Accepted: 53560
# Total Submissions: 142407
# Difficulty: Easy
# Contributors: Admin
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# 
# Example:
# Given num = 16, return true. Given num = 5, return false.
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:
# Special thanks to @yukuairoy for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        while start < num:
            start = start * 4
        return start == num
        
