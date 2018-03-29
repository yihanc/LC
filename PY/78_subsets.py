# Given a set of distinct integers, nums, return all possible subsets.
# 
# Note: The solution set must not contain duplicate subsets.
# 
# For example,
# If nums = [1,2,3], a solution is:
# 
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 
# 
# Subset -> Always append; Pass right

# 2018.03.22
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(line, nums):
            res.append(line)
            for i, num in enumerate(nums):
                dfs(line + [num], nums[i+1:])
            
        if not nums: return []
        res = []
        dfs([], nums)
        return res


# 2017.04.05 Another short version
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(line, A):
            res.append(line)
            for i in xrange(len(A)):
                dfs(line + [A[i]], A[i+1:])
        res = []
        dfs([], nums)
        return res

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfsHelper(res, sorted(nums), []) 
        print(res)
        return res

    def dfsHelper(self, res, nums, line):
        print(line)
        res.append(line)
        for i, num in enumerate(nums):
            # line.append(num)
            self.dfsHelper(res, nums[i+1:], line + [num])  # Why using line.append() and line.pop() won't work?? Because line is passed by reference. After all operations. It is cleared to be empty. So we need to pass a new object line + [num] to keep the value.
            # line.pop()

if __name__ == "__main__":
    sol = Solution()
    sol.subsets([1,2,3])
