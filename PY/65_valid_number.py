# 65. Valid Number   QuestionEditorial Solution  My Submissions
# Total Accepted: 57002
# Total Submissions: 455174
# Difficulty: Hard
# Contributors: Admin
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
# 
# Subscribe to see which companies asked this question

# 2018.02.23 Rewrite
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)
        while i < n and s[i] == " ":  i += 1
        if i < n and s[i] in "+-": i += 1
        n_nm, n_pt = 0, 0
        while i < n and s[i] in "0123456789.":
            if s[i] in "0123456789": n_nm += 1
            else: n_pt += 1
            i += 1
        
        if n_nm == 0 or n_pt > 1: return False
        
        if i < n and s[i] == "e": 
            i += 1
            if i < n and s[i] in "+-": i += 1
            
            n_nm, n_pt = 0, 0
            while i < n and s[i] in "0123456789.":
                if s[i] in "0123456789": n_nm += 1
                else: n_pt += 1
                i += 1
            
            if n_nm == 0 or n_pt > 0: return False
        
        while i < n and s[i] == " ": i += 1
        
        return i == n
            

# Solving in 4 steps
# 1. skip the leading whitespaces;
# 2. check if the significand is valid. To do so, simply skip the leading sign and count the number of digits and the number of points. A valid significand has no more than one point and at least one digit.
# 3. check if the exponent part is valid. We do this if the significand is followed by 'e'. Simply skip the leading sign and count the number of digits. A valid exponent contain at least one digit.
# 4. skip the trailing whitespaces. We must reach the ending 0 if the string is a valid number.
#
#  Test cases:  [-+]?(([0-9]+(.[0-9]*)?)|.[0-9]+)(e[-+]?[0-9]+)?

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and s[i] in "+-":
            i += 1
        
        n_pt, n_nm = 0, 0
        while i < n and ((s[i] >= '0' and s[i] <= '9') or s[i] == '.'):
            if s[i] == '.':
                n_pt += 1
            else:
                n_nm += 1
            i += 1
        
        if n_pt > 1 or n_nm < 1:
            return False
        
        if i < n and s[i] == 'e':
            i += 1
            if i < n and s[i] in "+-":
                i += 1
            
            n_nm = 0
            while i < n and s[i] >= '0' and s[i] <= '9':
                n_nm += 1
                i += 1
            
            if n_nm < 1:
                return False
        
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return True
        else:
            return False
