# 493. Reverse Pairs Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 3198
# Total Submissions: 17172
# Difficulty: Hard
# Contributors:
# ckcz123
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# 
# You need to return the number of important reverse pairs in the given array.
# 
# Example1:
# 
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
# 
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# Subscribe to see which companies asked this question.


# 2018.01.09 Binary Index Tree Solution
# T(i) = T(i - 1) + C, C is the case that first element from nums[i-1], second is nums[i]
# Using BIT to store makes update and search log(n) for each operation
# The index() function returns index from sorted array + 1

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        copy = sorted(nums)
        bits = [ 0 for x in xrange(n + 1)]
        res = 0
        for num in nums:
            #print(num, self.getIndex(copy, 2 * num + 1),  self.getIndex(copy, num))
            res += self.search(bits, self.getIndex(copy, 2 * num + 1))
            self.insert(bits, self.getIndex(copy, num))
            #print(res, bits)
        return res

    def getIndex(self, nums, val):  # This index function need to return the left most ele that is >= val.
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if val > nums[m]:
                l = m + 1
            else:                   # Also handles duplicates
                r = m - 1
        return l + 1

    def search(self, bits, i):
        res = 0
        while i < len(bits):
            res += bits[i]
            i += i & -i
        return res
        
    
    def insert(self, bits, i):
        while i > 0:
            bits[i] += 1
            i -= i & -i
        
    

# 2017.05.19 Merge sort + cache
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo: return 0
            cnt = sort(lo, mid) + sort(mid, hi)
            cache = [ 0 for _ in xrange(hi - lo) ]
            i = j = mid
            k = 0
            for left in nums[lo:mid]:   # loop is o(n)
                while i < hi and left > 2 * nums[i]: i += 1
                cnt += i - mid
                while j < hi and left >= nums[j]:
                    cache[k] = nums[j]
                    j, k = j + 1, k + 1
                cache[k] = left
                k += 1
            cache[k:] = nums[j:hi]
            nums[lo:hi] = cache    # TLE if cache[:]
            return cnt
        return sort(0, len(nums))

# 2017.05.19 
# Naive two loops. TLE.
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0
        count = 0
        for i in xrange(n - 1):
            for j in xrange(i+1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count
