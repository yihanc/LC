# 327. Count of Range Sum Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 17252
# Total Submissions: 58809
# Difficulty: Hard
# Contributor: LeetCode
# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.
# 
# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.
# 
# Example:
# Given nums = [-2, 5, -1], lower = -2, upper = 2,
# Return 3.
# The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.


# 2017.05.18
# Merge sort.  online version
# For each left in first[lo:mid] I find all right in first[mid:hi] so that right - left lies in [lower, upper]. Because the halves are sorted, these fitting right values are a subarray first[i:j]. With increasing left we must also increase right, meaning must we leave out first[i] if it's too small and and we must include first[j] if it's small enough.
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def sort(lo, hi):
            mid = (lo + hi) // 2
            if lo == mid: return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left < lower: i += 1
                while j < hi and first[j] - left <= upper: j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count
        
        first = [0]
        for num in nums:
            first.append(first[-1] + num)
        return sort(0, len(first))

# 2017.05.16
# Naive o(n**2). TLE for large case
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in xrange(n):
            for j in xrange(i, n):
                cur = sum(nums[i:j+1])
                if cur >= lower and cur <= upper:
                    count += 1
        return count
                
