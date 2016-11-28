# 67. Add Binary  QuestionEditorial Solution  My Submissions
# Total Accepted: 106242
# Total Submissions: 361409
# Difficulty: Easy
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100".

# 11.27.2016. Rewrite.
# Padding "0" solution. Easier and more clear
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        
        if m > n:
            b, n = "0" * (m - n) + b, m
        else:
            a, m = "0" * (n - m) + a, n
        
        res = ""
        carry = 0
        for i in xrange(m-1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            if sum >= 2:
                carry = 1
            else:
                carry = 0
            
            if sum % 2 == 0:
                res = "0" + res
            else:
                res = "1" + res
        
        return res if carry == 0 else "1" + res
            
        

# Better Solution. Don't care about the order
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        i, j = len(a) -1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry == 1:
            tmp = 0
            if i >= 0:
                tmp += int(a[i])
            if j >= 0:
                tmp += int(b[j])
            if carry == 1:
                tmp += carry
                
            res = str(tmp % 2) + res
            
            if tmp >= 2:
                carry = 1
            else:
                carry = 0
                
            i -= 1
            j -= 1
        
        return res


if __name__ == "__main__":
    print(Solution().addBinary("1", "1"))
    
