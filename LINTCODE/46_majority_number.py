class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        candidate = None
        count = 0
        for num in nums:
            if not candidate or (candidate and count == 0):
                candidate, count = num, count + 1
                continue
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
