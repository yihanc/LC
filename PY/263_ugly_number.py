# 263. Ugly Number Add to List
# Description  Submission  Solutions
# Total Accepted: 90580
# Total Submissions: 234957
# Difficulty: Easy
# Contributors: Admin
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# 
# Note that 1 is typically treated as an ugly number.
# 
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# num <= 0 are not ugly
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num <= 5 and num != 4:
            return True
            
        while num % 2 == 0 and num != 1:
            num = num // 2
            print(num)
        
        while num % 3 == 0 and num != 1:
            num = num // 3
            print(num)
        
        while num % 5 == 0 and num != 1:
            num = num // 5
            print(num)
        
        return True if num == 1 else False

if __name__ == "__main__":
    num = -2147483648
    print(Solution().isUgly(num))
