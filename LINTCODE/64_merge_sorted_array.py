# 64. Merge Sorted Array 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# 
#  Notice
# 
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
# 
# Have you met this question in a real interview? Yes
# Example
# A = [1, 2, 3, empty, empty], B = [4, 5]
# 
# After merge, A will be filled as [1, 2, 3, 4, 5]


# 2017.12.11
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        if j != -1:
            A[:j+1] = B[:j+1]
        
