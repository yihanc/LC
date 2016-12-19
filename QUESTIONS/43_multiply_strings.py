# 43. Multiply Strings My Submissions QuestionEditorial Solution
# Total Accepted: 63764 Total Submissions: 267423 Difficulty: Medium
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.
# Subscribe to see which companies asked this question

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return "0"
        if num1 == "1": return num2
        if num2 == "1": return num1
        
        n1, n2 = len(num1), len(num2)
        res = [ 0 for x in xrange(n1 + n2)]
        
        for i in xrange(n1):
            for j in xrange(n2):
                cur = int(num1[i]) * int(num2[j])
                if cur >= 10:
                    res[i+j] += cur // 10
                res[i+j+1] += cur % 10

        print(res)
        
        i = 0
        while res[i] == 0:
            i += 1
        
        res2 = ""
        while i < n1 + n2:
            res2 += str(res[i])
            i += 1
        return res2


if __name__ == "__main__":
    #print(Solution().multiply("2", "3"))
    #print(Solution().multiply("98", "9"))
    print(Solution().multiply("123", "456"))
