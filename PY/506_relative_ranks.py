# 506. Relative Ranks Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14153
# Total Submissions: 30158
# Difficulty: Easy
# Contributors:
# taylorty
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
# 
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

# 2017.05.26
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = [ "" for x in xrange(len(nums)) ]
        s_nums = sorted(enumerate(nums), key = lambda x: (x[1], x[0]), reverse=True)
        for i in xrange(len(s_nums)):
            oi, num = s_nums[i]
            if i == 0: res[oi] = "Gold Medal"
            elif i == 1: res[oi] = "Silver Medal"
            elif i == 2: res[oi] = "Bronze Medal"
            else: res[oi] = str(i+1)
        return res
            
