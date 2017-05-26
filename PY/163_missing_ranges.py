# 163. Missing Ranges Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 26794
# Total Submissions: 105956
# Difficulty: Medium
# Contributor: LeetCode
# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# 
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].


# 2017.05.21
# Online clean version
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for n in nums:
            justBelow = n - 1
            if lower == justBelow: res.append(str(lower))
            elif lower < justBelow: res.append(str(lower) + "->" + str(justBelow))
            lower = n + 1
        if lower == upper: res.append(str(lower))
        elif lower < upper: res.append(str(lower) + "->" + str(upper))
        return res
