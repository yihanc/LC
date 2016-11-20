# 43. Multiply Strings My Submissions QuestionEditorial Solution
# Total Accepted: 63764 Total Submissions: 267423 Difficulty: Medium
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.
# Subscribe to see which companies asked this question

# This passed OJ
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = ""
        sum = 0

        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                print(mul)
                sum +=  mul * (10**(m-i-1+n-j-1))
                print(sum)
        
        return str(sum)

if __name__ == "__main__":
    #print(Solution().multiply("2", "3"))
    print(Solution().multiply("98", "9"))
#    print(Solution().multiply("123", "456"))
