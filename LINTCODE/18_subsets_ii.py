class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        def _dfs(line, nums):
            res.append(line)
            
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                _dfs(line + [num], nums[i+1:])
        
        nums.sort()
        res = []
        _dfs([], nums)
        return res
