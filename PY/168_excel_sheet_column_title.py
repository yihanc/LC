# 168. Excel Sheet Column Title   QuestionEditorial Solution  My Submissions
# Total Accepted: 81461
# Total Submissions: 340134
# Difficulty: Easy
# Contributors: Admin
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

#2017.03.11 Rewrite
import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic = []
        for char in string.uppercase:
            dic.append(char)
        
        res = ""
        while n >= 1:
            n = n - 1
            res = dic[n % 26] + res
            n = n // 26
        return res


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: return ""
        
        res = ""
        while n > 26:
            c = chr(ord('A') + (n - 1) % 26 )
            res = c + res
            n = (n - 1) // 26
        
        res = chr(ord('A') + (n - 1) % 26 ) + res
        return res
            
