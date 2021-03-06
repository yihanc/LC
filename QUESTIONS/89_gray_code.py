# 89. Gray Code   QuestionEditorial Solution  My Submissions
# Total Accepted: 74399
# Total Submissions: 192051
# Difficulty: Medium
# Contributors: Admin
# The gray code is a binary numeral system where two successive values differ in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
# 
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# 
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
# 
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
            
        res = [0, 1]
        i = 0
        while n - i > 1:
            tmp = res[:]
            for num in tmp[::-1]:
                res.append(num + (2 << i))      # Need () around 2<<i
            i += 1
        return res
