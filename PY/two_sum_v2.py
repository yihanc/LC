class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        ans = []
        for i, num in enumerate(nums):
            if target - num not in dict:
                dict[num] = i
            else:
                ans.append(dict[target - num] + 1)
                ans.append(i + 1)
                return ans
