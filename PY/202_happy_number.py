# 202. Happy Number Add to List
# Description  Submission  Solutions
# Total Accepted: 108823
# Total Submissions: 275266
# Difficulty: Easy
# Contributors: Admin
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# 
# Example: 19 is a happy number
# 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# 2017.02.20 Detect LL cycle method
class Solution(object):
    def squareRootSum(self, n):
        res = 0
        while n > 0:
            digit = n % 10
            res += digit * digit
            n = n // 10
        return res
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        while True:
            slow = self.squareRootSum(slow)
            fast = self.squareRootSum(fast)
            fast = self.squareRootSum(fast)
            if fast == 1: return True
            if slow == fast: break
        
        return False


# 2017.02.20 Dic method
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {'0': True}
        summ = 0
        while summ != 1:
            summ = 0
            digits = []
            tmp = n
            while tmp > 0:
                summ += (tmp % 10) ** 2
                digits.append(str(tmp % 10))
                tmp = tmp // 10
            digits.sort()
            key = ''.join(digits)
            if key in dic:
                return False
            else:
                dic[key] = True
            n = summ
            
        return True

