# 66. Plus One  QuestionEditorial Solution  My Submissions
# Total Accepted: 127699
# Total Submissions: 355449
# Difficulty: Easy
# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.

# 2017.05.11
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            csum = digits[i] + carry
            digits[i] = csum % 10
            if csum >= 10: 
                carry = 1
            else:
                carry = 0
                break
        return digits if carry == 0 else [1] + digits
        
            

# 11.26.2016 Rewrite. Better and clearer
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]
        
        n = len(digits)
        carry = 1
        for i in xrange(n-1, -1, -1):
            digits[i] = digits[i] + carry
            if digits[i] == 10:
                digits[i], carry = 0, 1
            else:
                carry = 0
                
        return [1] + digits if carry == 1 else digits


class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        i = len(digits) - 1
        
        while i >= 0:
            tmp = 0
            if i == len(digits) - 1:
                tmp = 1
            
            if digits[i]:
                tmp += digits[i]
            if carry > 0:
                tmp += carry
                
            if tmp >= 10:
                carry = 1
                tmp = tmp % 10
            else:
                carry = 0
                
            digits[i] = tmp
            i -= 1
        
        if carry > 0:
            return [1] + digits
        else:
            return digits
