# 8. String to Integer (atoi) My Submissions QuestionEditorial Solution
# Total Accepted: 102154 Total Submissions: 756574 Difficulty: Easy
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
# 
# spoilers alert... click to show requirements for atoi.
# 
# Subscribe to see which companies asked this question

# 2018.02.25

# Analysis
# 1. leading space
# 2. sign
# 3. overflow
# 4. invalid input
# http://www.cplusplus.com/reference/cstdlib/atoi/

# 2016.11.18
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        res = 0
        
        i = 0
        while i < len(str) and str[i] == " ": 
            i += 1
        
        if i < len(str) and str[i] == "+":
            i += 1
        elif i < len(str) and str[i] == "-":
            sign = -1
            i += 1
            
        while i < len(str) and str[i] in "0123456789":
            if sign == 1 and ((res > 214748364) or (res == 214748364 and ord(str[i]) - ord("0") > 7)):
                return 2147483647
            if sign == -1 and ((res > 214748364) or (res == 214748364 and ord(str[i]) - ord("0") > 8)):
                return -2147483648
                
            res = res * 10 + ord(str[i]) - ord("0")
            i += 1
            
        return res * sign
            
            

class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n, int_max, int_min = len(str), 2147483647, -2147483648
        if n == 0: return 0

        # Discard leading space
        i = 0
        while i < n and str[i] == ' ':
            i += 1

        # Detect sign
        sign = 1
        if str[i] == "-": sign = -1
        if str[i] == "+" or str[i] == "-": i += 1

        # Check if input is valid
        base = 0
        while i < n and str[i] in "0123456789":
            digi = ord(str[i]) - ord('0')
            if sign == 1 and (base > 214748364 or ( base == 214748364 and digi > 7)):
                return int_max
            elif sign == -1 and (base > 214748364 or (base == 214748364 and digi > 8)):
                return int_min
            base = 10 * base + ord(str[i]) - ord('0')
            i += 1

        return base * sign

if __name__ == "__main__":
    sol = Solution()
#    print(sol.myAtoi("-2147483647"))
    print(sol.myAtoi("      -11919730356x"))
