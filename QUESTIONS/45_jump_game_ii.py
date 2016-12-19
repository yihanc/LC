# 45. Jump Game II  QuestionEditorial Solution  My Submissions
# Total Accepted: 74211
# Total Submissions: 287225
# Difficulty: Hard
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# For example:
# Given array A = [2,3,1,1,4]
# 
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
# 
# Note:
# You can assume that you can always reach the last index.
# 
# Subscribe to see which companies asked this question

# 12.18.2016 Rewrite DP solution. 
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0
        dp = [ n + 1 for x in xrange(n) ]
        dp[0] = 0
        maxreach = 0
        
        for i in xrange(n):
            if nums[i] + i <= maxreach:		# When to skip
                continue
            else:
                maxreach = nums[i] + i
            
            for j in xrange(i + 1, maxreach + 1): 	# For nums[i], update dp[j]
                if j < n:
                    dp[j] = min(dp[j], dp[i] + 1)
                
                if j >= n - 1:
                    return dp[-1]
        return dp[-1]


# Using curS, curE, nextS, nextE 4 pointers
# Time complexity? O(N)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        n = len(nums)
        level, curS, curE, nextS, nextE = 0, 0, 1, 1, 1
        
        while nextE < len(nums):
            nextS = curE 
            for i in xrange(curS, curE):
                nextE = max(nextE, i + nums[i] + 1)
            curS, curE = nextS, nextE
            level += 1
        return level
            
if __name__ == "__main__":
    print(Solution().jump([0]))
    print(Solution().jump([2,3,1,1,4]))
    print(Solution().jump([1,1,1,1,4]))
