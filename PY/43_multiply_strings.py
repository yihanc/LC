# 43. Multiply Strings My Submissions QuestionEditorial Solution
# Total Accepted: 63764 Total Submissions: 267423 Difficulty: Medium
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.
# Subscribe to see which companies asked this question

# 11.26.2016 Rewrite
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        if num1 == "0" or num2 == "0": return "0"
        if num1 == "1": return num2
        if num2 == "1": return num1
        
        res = 0
        
        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                res += mul * ( 10 ** (m - 1 -i + n - 1 -j ))
                print(mul, res)
                j -= 1
            i -= 1
        print(res)
        
        return str(res)
        
        

# This passed OJ
class Solution2(object):
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
    #print(Solution().multiply("123", "456"))
    #print(Solution().multiply("140", "721"))
