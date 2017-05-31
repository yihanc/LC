# 378. Kth Smallest Element in a Sorted Matrix Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 34566
# Total Submissions: 78438
# Difficulty: Medium
# Contributor: LeetCode
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
# 
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# 
# Example:
# 
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.

# 2017.05.29
# heapq merge merge multiple sorted input
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return list(heapq.merge(*matrix))[k-1]

# Use a heapq n smallest
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        hq = []
        for row in matrix:
            hq += row
        hq = heapq.nsmallest(k, hq)
        #print(tmp)

        while len(hq) > 1:
            heapq.heappop(hq)
        return hq[0]
            
            
