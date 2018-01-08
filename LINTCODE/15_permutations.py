class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        def _dfs(line, nums):
            if not nums:
                res.append(line)
                return
            
            for i, num in enumerate(nums):
                _dfs(line + [num], nums[:i] + nums[i+1:])
            
        res = []
        _dfs([], nums)
        return res
