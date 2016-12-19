# 137. Single Number II  QuestionEditorial Solution  My Submissions
# Total Accepted: 98617
# Total Submissions: 250008
# Difficulty: Medium
# Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [ 0 for x in xrange(32) ]

        for num in nums:
            tmp = num
            i = 0
            while tmp != 0:
                bits[i] += (tmp % 2)
                tmp = tmp >> 1
                i += 1

        print(bits)
        res = 0
        for i in xrange(32):
            if bits[i] % 3 == 1:
                res += (1 << i)

        return res

if __name__ == "__main__":
    nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
#    nums = [1,1,1,3,3,3,2,2,2,4]
    print(Solution().singleNumber(nums))
