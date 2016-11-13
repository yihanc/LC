# 171. Excel Sheet Column Number   QuestionEditorial Solution  My Submissions
# Total Accepted: 106753
# Total Submissions: 239110
# Difficulty: Easy
# Contributors: Admin
# Related to question Excel Sheet Column Title
# 
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# 
# For example:
# 
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        
        for c in s:
            res = res * 26 + ord(c) - 64
        
        return res
        
