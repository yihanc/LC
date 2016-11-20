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
# Analysis
# 1. leading space
# 2. sign
# 3. overflow
# 4. invalid input
# http://www.cplusplus.com/reference/cstdlib/atoi/
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
