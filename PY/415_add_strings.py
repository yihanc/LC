# 415. Add Strings Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 31626
# Total Submissions: 76829
# Difficulty: Easy
# Contributor: LeetCode
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# 2017.05.23
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        if n1 <= n2: num1 = "0" * (n2 - n1) + num1
        else: num2 = "0" * (n1 - n2) + num2
        
        res = ""
        carry = 0
        i = max(n1, n2) - 1
        while i >= 0:
            c1 = ord(num1[i]) - ord('0')
            c2 = ord(num2[i]) - ord('0')
            tmp = c1 + c2 + carry
            if tmp >= 10:
                carry = 1
            else:
                carry = 0
            res = str(tmp % 10) + res
            i -= 1
        return res if carry == 0 else "1" + res
            
