# 182. Delete Digits 
# Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.
# 
# Find the smallest integer after remove k digits.
# 
# N <= 240 and k <= N,
# 
# Have you met this question in a real interview? Yes
# Example
# Given an integer A = "178542", k = 4
# 
# return a string "12"

from collections import deque
class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, l):
        # write your code here
        if not A or len(A) == 0 or len(A) == l: return ""
        d = deque()
        k = 0
        res = ""
        for i in xrange(len(A)):
            while k < l and d and d[-1] > A[i]:
                d.pop()
                k += 1
            d.append(A[i])
        
        while k < l:
            d.pop()
            k += 1
        
        while d and d[0] == "0": 
            d.popleft()
        
        return "".join(list(d))
        
        
