class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        def _dfs(line, nums):
            if not nums:
                res.append(line)
                return
            
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                
                _dfs(line + [num], nums[:i] + nums[i+1:])
            
        
        nums.sort()
        res = []
        _dfs([], nums)
        return res
