def removeDuplicates(nums):
    # write your code here
    if len(nums) <= 1: return nums
    i, n = 1, len(nums)
    while i < n:
        if nums[i] == nums[i-1]:
            del nums[i]
            n -= 1
            continue
        i += 1
    return len(nums)

nums = [1,1,2]
print(nums)
print(removeDuplicates(nums))
print(nums)
