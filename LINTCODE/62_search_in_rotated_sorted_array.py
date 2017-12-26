
class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or len(A) == 0: return -1
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                return mid
            elif (( target > A[mid] and target <= A[-1] ) or 
                ( A[mid] > A[-1] and (target > A[mid] or target <= A[-1] ))):
                l = mid + 1
            else:
                r = mid - 1
        return -1
