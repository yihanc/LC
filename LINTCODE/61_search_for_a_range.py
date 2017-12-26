class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A or len(A) == 0: return [-1, -1]
        res = [-1, -1]
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target and (mid == 0 or A[mid-1] != target):
                res[0] = mid
                break
            elif target > A[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        if res[0] == -1: return [-1, -1]
        l, r = res[0], len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target and (mid == len(A) - 1 or A[mid+1] != target):
                res[1] = mid
                return res
            elif target < A[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
                
                
