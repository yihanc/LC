# 79. Longest Common Substring 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given two strings, find the longest common substring.
# 
# Return the length of it.
# 
#  Notice
# 
# The characters in substring should occur continuously in original string. This is different with subsequence.
# 
# Have you met this question in a real interview? Yes
# Example
# Given A = "ABCD", B = "CBCE", return 2.


# Mon Dec 11 12:21:58 EST 2017
class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if A is None or B is None: return 0
        res = 0
        i = 0
        while i < len(A):
            j = 0
            while j < len(B):
                count = 0
                while (i + count < len(A) and j + count < len(B) and A[i+count] == B[j+count]):
                    count += 1
                res = max(res, count)
                j += 1
            i += 1
        return res
            
