# 47. Permutations II My Submissions QuestionEditorial Solution
# Total Accepted: 72793 Total Submissions: 257518 Difficulty: Medium
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
# 
# Subscribe to see which companies asked this question

# 2018.03.22
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(line, nums):
            if len(nums) == 0: res.append(line)
            
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]: 
                    continue
                dfs(line + [num], nums[:i] + nums[i+1:])
                
        if not nums: return []
        res = []
        nums.sort()
        dfs([], nums)
        return res


class Solution(object):
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)

        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                self.dfs(nums[:i]+nums[i+1:], res, path+[nums[i]])

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, res, [])
        print(res)
        return res

if __name__ == "__main__":
    Solution().permuteUnique([1,1,2])
    Solution().permuteUnique([1,5,1])
    Solution().permuteUnique([5,1,1])
    Solution().permuteUnique([1,1,1])
