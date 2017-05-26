# 307. Range Sum Query - Mutable Add to List
# Description
# Hints
# Submissions
# Solutions
# Total Accepted: 31129 Total Submissions: 157574 Difficulty: Medium
# Contributor: LeetCode
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.


# 2017.05.21
# BIT
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums: return
        self.n = len(nums)
        self.tree = [ 0 for x in xrange(self.n + 1) ]
        self.nums = [ 0 for x in xrange(self.n) ]   # To update delta
        for i in xrange(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def _sum(index):
            res = 0
            index += 1
            while index > 0:
                res += self.tree[index]
                index -= index & (-index)
            return res
        print(j, _sum(j), i-1, _sum(i-1))
        return _sum(j) - _sum(i-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

