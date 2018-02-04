# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
# 
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
# 
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
# 
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).


# TLE for Large Case
# DFS + presum array
# O(1) to fetch range sum from presum array
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # print(nums, k)
        if len(nums) < k * 3 or k == 0: return 0
        sums = [ 0 ]
        for i in xrange(len(nums)):
            sums.append(sums[i] + nums[i])
        # print(sums)
        res = [0, [0, k, 2*k]]        # res saves the index of the current largest
        self.dfs(res, nums, [], k, sums, 0)
        return res[1]

    def dfs(self, res, nums, line, k, sums, start):
        #print("----- dfs ", line, start)
        if len(line) == 3:
            cursum = sum([self.getRangeSum(sums, i, i+k-1) for i in line])
            # print(cursum)
            if cursum > res[0]:
                res[0], res[1] = cursum, line
                print("update res ", res)
            return

        for i in xrange(start, max(0, len(nums) - (3-len(line)) * k + 1)):
            self.dfs(res, nums, line + [i], k, sums, i + k)

    def getRangeSum(self, sums, start, end):
        # print("SUMS: ",sums, start, end, sums[end+1] - sums[start])
        return sums[end+1] - sums[start]



# nums, k = [1,2,1,2,6,7,5,1], 2
# expected = [0, 3, 5]

# nums, k = [7,13,20,19,19,2,10,1,1,19], 3
# expected = [0, 3, 5]

# Large case
nums, k = [44373,10902,54583,23982,31189,18028,10447,32387,57284,61499,48093,57979,47480,26312,62335,53637,4055,19560,4208,62393,7072,37542,19812,35711,55461,16899,45550,19301,5190,57443,18711,34905,4023,10431,9690,26965,18236,45857,62769,60437,7138,59957,40155,30823,58611,25709,30652,58397,42,8199,22332,3645,60973,50944,61379,33402,11115,51889,58276,46604,51978,15636,62567,60521,33383,33669,43713,9304,15467,57391,6099,31735,26581,57868,7384,57203,64825,50089,21298,53160,40111,38169,63041,42401,12825,12365,29538,55419,19122,18857,37521,7328,5532,55422,60920,40138,59638,17313,43762,9649,45725,40934,33194,49171,17663,41901,65157,53563,37914,27740,47319,26205,62322,11920,42586,31817,3986,40938,62862,63054,58280,15101,44332,26850,25732,44850,53066,23564,15754,43132,11287,21229,38871,36316,50353,46771,17264,61070,36522,37914,56260,44994,48868,32221,37207,6703,17231,14762,31900,51154,3232,62798,14262,15408,49826,63684,8429,34507,19054,30767,30019,59130,33344,30461,57187,44212,7465,14989,23038,24672,58440,52652,16636,50260,36647,57975,19058,43570,62997,19620,58851,59853,30051,30794,25111,7341,20900,61163,62326,44343,9742,34722,6981,55058,11730,20319,59715,3464,11600,53653], 3

print(nums, k)
# print(expected)
print(Solution().maxSumOfThreeSubarrays(nums, k))
