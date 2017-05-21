import random

from heapq import *
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def mergesort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo: return
            mergesort(lo, mid)
            mergesort(mid, hi)
            left, right = lo, hi - 1
            while left < mid and right >= mid:
                cur = first[right] - first[left]
                print(cur, hq)
                if cur <= k and (not hq or cur > -hq[0]):
                    heappush(hq, -cur)
                
                #print(lo, mid, hi, first, left, right)
                if (left == mid - 1 or (left + 1 < mid and right - 1 >= mid and 
                    first[right-1] - first[left] > first[right] - first[left+1])):
                    right -= 1
                else:
                    left += 1
            first[lo:hi] = sorted(first[lo:hi])
                
        print(matrix)
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        hq, cmax = [], float('-inf')
        for l in xrange(n):
            nums = [ 0 for i in xrange(m) ]
            for r in xrange(l, n):
                first = [0]
                for i in xrange(m):
                    nums[i] += matrix[i][r]
                    first.append(first[-1] + nums[i])
                mergesort(0, len(first))
        return -heappop(hq) if hq else 0

            
if __name__ == "__main__":
    matrix = [
                [-9, -6, -1, -7, -6, -5, -4, -7, -6, 0], 
                [-4, -9, -4, -7, -7, -4, -4, -6, -6, -6], 
                [-2, -2, -6, -7, -7, 0, -1, -1, -8, -2], 
                [-5, -3, -1, -6, -1, -1, -6, -3, -4, -8], 
                [-4, -1, 0, -8, 0, -9, -8, -7, -2, -4], 
                [0, -3, -1, -7, -2, -5, -5, -5, -8, -7], 
                [-2, 0, -8, -2, -9, -2, 0, 0, -9, -6], 
                [-3, -4, -3, -7, -2, -1, -9, -5, -7, -2], 
                [-8, -3, -2, -8, -9, 0, -7, -8, -9, -3], 
                [-7, -4, -3, -3, -3, -1, 0, -1, -8, -2]
            ]

    k = -321

    m, n = len(matrix), len(matrix[0])
    for si in xrange(m):
        for sj in xrange(n):
            for ei in xrange(si, m):
                for ej in xrange(sj, n):
                    summ = 0
                    for row in matrix[si:ei+1]:
                        summ += sum(row[sj:ej+1])
                    print((si, sj), (ei, ej), summ)


    # print(Solution().maxSumSubmatrix(matrix, k))
