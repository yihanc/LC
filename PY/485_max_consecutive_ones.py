class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
            res = max(res, count)
        return res
