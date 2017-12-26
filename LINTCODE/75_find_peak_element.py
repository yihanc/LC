# 75. Find Peak Element 
# There is an integer array which has the following features:
# 
# The numbers in adjacent positions are different.
# A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
# We define a position P is a peak if:
# 
# A[P] > A[P-1] && A[P] > A[P+1]
# Find a peak element in this array. Return the index of the peak.
# 
#  Notice
# It's guaranteed the array has at least one peak.
# The array may contain multiple peeks, find any of them.
# The array has at least 3 numbers in it.

class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A or len(A) == 0: raise Exception("Input is empty or not valid")
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if (( mid == 0 or A[mid] > A[mid - 1] ) and 
                ( mid == len(A) - 1 or A[mid] > A[mid + 1])):
                return mid
            elif mid != 0 and A[mid] <= A[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
                
                
