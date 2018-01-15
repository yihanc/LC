def maxArray1(nums, k):    # Get K maximum from nums, 
    n = len(nums)
    res = [0] * k
    j = 0
    for i in xrange(n):
        # n - i > k - j, nums has n - i items left, need to fetch k - j items
        print(i, j)
        while n - i + j > k and j > 0 and res[j-1] < nums[i]:
            j -= 1
        if j < k:       
            res[j] = nums[i]
            j += 1
        print("res ", res)
    return res

def maxArray2(nums, k):    # Get K maximum from nums
    res = [ 0 for j in xrange(k) ]
    pos = -1 # Last index
    for j in xrange(k): # j pointer for res, i pointer in nums
        left = k - j    # Still need to find left elements
        i = pos + 1
        while len(nums) - i >= left:
            if nums[i] > res[j]:
                res[j] = nums[i]
                pos = i
            i += 1
    return res

nums = [8,6,5,4,10,4]
print(nums)
k = 3
maxArray1(nums, k)
