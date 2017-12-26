# 183. Wood Cut 
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
# 
#  Notice
# You couldn't cut wood into float length.
# 
# If you couldn't get >= k pieces, return 0.
# 
# Have you met this question in a real interview? Yes
# Example
# For L=[232, 124, 456], k=7, return 114.

class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or len(L) == 0: return 0
        max_len = max(L)
        res = 0
        l, r = 1, max_len
        while l <= r:
            mid = (l + r) // 2
            piece_sum = sum(map(lambda x: x // mid, L))
            if piece_sum >= k:
                res = max(mid, res)
                l = mid + 1
            else:
                r = mid - 1
        return res
