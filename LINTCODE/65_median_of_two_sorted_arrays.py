
# 1.1.2018
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        if m > n: 
            return self.findMedianSortedArrays(B, A)
        
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            
            if i > 0 and j < n and A[i-1] > B[j]:
                r = i - 1
            elif i < m and j > 0 and B[j-1] > A[i]:
                l = i + 1
            else:
                if i == 0: mid1 = B[j-1]
                elif j == 0: mid1 = A[i-1]
                else: mid1 = max(A[i-1], B[j-1])
                B
                if (m + n) % 2 == 1: return mid1
                
                if i == m: mid2 = B[j]
                elif j == n: mid2 = A[i]
                else: mid2 = min(A[i], B[j])
                
                return (mid1 + mid2) / 2.0
                    
