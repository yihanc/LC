# 81. Data Stream Median 
# Numbers keep coming, return the median of numbers at every time a new number added.
# 
# Have you met this question in a real interview? Yes
# Clarification
# What's the definition of Median?
# - Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
# 
# Example
# For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].
# 
# For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].
# 
# For numbers coming list: [2, 20, 100], return [2, 2, 20].
# 
# Challenge 
# Total run time in O(nlogn).

# 12.30.2017
# Two heapq
from heapq import *

class Solution:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        big = []
        small = []
        
        res = []
        
        for num in nums:
            heappush(big, num)
            heappush(small, -heappop(big))
            if len(small) > len(big):
                heappush(big, -heappop(small))
            if len(small) < len(big):
                res.append(big[0])
            else:
                res.append(-small[0])
        return res
