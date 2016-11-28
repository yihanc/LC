# 152. Maximum Product Subarray My Submissions QuestionEditorial Solution
# Total Accepted: 60873 Total Submissions: 271144 Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
# Subscribe to see which companies asked this question

# 11.26.2016 Rewrite
# Similar algorithm to Maximum Subarray.
# Travese
# 1. curMax = max(nums[i], curMax * nums[i]) or max(nums[i], curMin * nums[i]) for < 0
# 2. curMin = min(nums[i], curMin * nums[i]) or min(nums[i], curMax * nums[i]) for < 0
# 3. Update preMax = max(preMax, curMax)
# Some bug notes:
# 1. xrange(1, n) not xrange(n)
# 2. curMax, curMin need to be calculated at the same line. Otherwise wrong

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        preMax, curMax = nums[0], nums[0]
        curMin = nums[0]
        
        for i in xrange(1, n):
            if nums[i] > 0:
                curMax, curMin = max(nums[i], curMax * nums[i]), min(nums[i], curMin * nums[i])
            else:
                curMax, curMin = max(nums[i], curMin * nums[i]),  min(nums[i], curMax * nums[i])

            preMax = max(preMax, curMax)
        return preMax


# Record max and min.
# If < 0, mx = last max and min * cur)
# if > 0, mx = 
# DP
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        cur_max = cur_min = res = nums[0]
        
        i = 1
        while i < len(nums):
            tmp_max = max(nums[i],  max(cur_max * nums[i], cur_min * nums[i]))
            tmp_min = min(nums[i],  min(cur_max * nums[i], cur_min * nums[i]))
            cur_max, cur_min = tmp_max, tmp_min
            res = max(res, cur_max)
            i += 1
        return cur_max

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual( Solution().maxProduct([-4,-3,-2]), 12 )
        self.assertEqual( Solution().maxProduct([-2,0,-1]), 2)

if __name__ == "__main__":
    unittest.main()
