# 189. First Missing Positive 
# Given an unsorted integer array, find the first missing positive integer.
# 
# Have you met this question in a real interview? Yes
# Example
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        
        i = 0
        while i < len(A):
            while A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i] - 1]:
                j = A[i] - 1
                A[i], A[j] = A[j], A[i]
            i += 1
        
        for i, num in enumerate(A):
            if num != i + 1:
                return i + 1
        return len(A) + 1
            


