# 184. Largest Number 
# Given a list of non negative integers, arrange them such that they form the largest number.
# 
#  Notice
# The result may be very large, so you need to return a string instead of an integer.
# 
# Have you met this question in a real interview? Yes
# 

class Solution:
    """
    @param: nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        # One liner
        s_nums = map(lambda x: str(x), nums)
        res = "".join(sorted(s_nums, cmp=lambda x, y: cmp(y+x, x+y)))
        return "0" if int(res) == 0 else res
