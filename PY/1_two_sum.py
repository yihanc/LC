class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}        # 1
        for i, num in enumerate(nums):      # o(3n) = o(n)
            if target - num in dic:             # o(1)
                return (dic[target-num], i+1)       o(1)
            dic[num] = i+1          # o(1), 
