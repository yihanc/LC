# 367. Valid Perfect Square Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 39118
# Total Submissions: 103148
# Difficulty: Easy
# Contributor: LeetCode
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# Input: 16
# Returns: True
# Example 2:
# 
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            #print(l, r, mid)
            if mid * mid == num: 
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
