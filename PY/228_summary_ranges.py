# 228. Summary Ranges Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 74891
# Total Submissions: 258513
# Difficulty: Medium
# Contributor: LeetCode
# Given a sorted integer array without duplicates, return the summary of its ranges.
# 
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

# 2017.05.05, i for start, j for end
# if j - i == 1, just one element
# else, insert range
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] - nums[i] == j - i:
                j += 1
            if j - i == 1: res.append(str(nums[i]))
            else: res.append(str(nums[i]) + "->" + str(nums[j-1]))
            i = j
        return res
            
