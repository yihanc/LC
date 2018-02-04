# 679. 24 Game
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
# 
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.


# 2018.02.04
# Basic DFS
# Special case, when left 2 elements, we need to check the result from other two element first by saving the existing result. 

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.dfs(nums, None, None)

    # "save" is only needed when handling similar case of (a +/- b) * or /  (c +/- d).
    # However, this solution is not checking those symbols. Some further optimization can be made to reduce the redundant works.
    def dfs(self, nums, cur, save):
        if not nums and save is None and self.is24(cur): return True
            
        if not nums and save and self.dfs([save], cur, None): return True
            
        for i in xrange(len(nums)):
            num, next_nums = nums[i], nums[:i] + nums[i+1:]
            
            if cur is None:                                        # BUG, if not cur, just set the cur.
                if self.dfs(next_nums, num, save): return True
            else:
                next_cur = [cur + num, cur - num, cur * num, float(cur) / num, num - cur]
                if cur != 0: next_cur += [float(num) / cur]
            
                for x in next_cur:
                    if self.dfs(next_nums, x, save): return True
                    if len(nums) == 3 and self.dfs(next_nums, None, x): return True        # Case (1 + 9) * (1 + 2)
        return False
            

    def is24(self, x):
        return True if x == 24 or abs(24 - x) < 0.00001 else False
        
