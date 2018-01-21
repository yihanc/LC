def maxSubarray(nums):
    print(nums)
    if not nums: return 0
    res, cur = nums[0], nums[0]
    for i in xrange(1,len(nums)):
        cur = max(cur + nums[i], nums[i])
        res = max(res, cur)
    return res

nums = [3,5,-5,8]
print(maxSubarray(nums))
