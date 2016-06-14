# 46. Permutations My Submissions QuestionEditorial Solution
# Total Accepted: 101954 Total Submissions: 282174 Difficulty: Medium
# Given a collection of distinct numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# 

# Better way. Remove num[i] for each DFS. No need for DIC
class Solution(object):
    def dfs(self, nums, res, line):
        if not nums:
            print(line)
            res.append(line)
            return 

        for i, num in enumerate(nums):
            # line.append(num)
            self.dfs(nums[:i]+nums[i+1:], res, line+[num])      # Note line+[num] here. Use line.append(num) and line.pop() after won't work
            # self.dfs(nums[:i]+nums[i+1:], res, line) 
            # line.pop()
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        line = []
        self.dfs(nums, res, line)
        print(res)
        return res

if __name__ == "__main__":
    Solution().permute([1,2])
