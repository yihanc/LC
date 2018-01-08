# 315. Count of Smaller Numbers After Self Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 30573 Total Submissions: 89588 Difficulty: Hard Contributor: LeetCode
# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# 
# Example:
# 
# Given nums = [5, 2, 6, 1]
# 
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

# 2017.01.07 BST Insert solution. Easy
# Each node has
# 1. left sum for total number of nodes to its left
# 2. dup for how many for the current node
# When inserting, if == node.val, dup + 1
# If less, insert left, node.sum ++
# If more, insert right, update pre_sum += node.sum, node.dup

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [ 0 for x in xrange(len(nums))]
        root = None
        for i in xrange(len(nums)-1, -1, -1):
            root = self.insert(nums[i], root, res, i, 0)
        return res

    def insert(self, num, node, res, i, pre_sum):
        if not node:
            node = Node(num, 0)
            res[i] = pre_sum
        elif node.val == num:
            node.dup += 1
            res[i] = pre_sum + node.sum
        elif node.val > num:
            node.sum += 1
            node.left = self.insert(num, node.left, res, i, pre_sum)
        else:
            node.right = self.insert(num, node.right, res, i, pre_sum + node.dup + node.sum)
        return node

class Node:
    def __init__(self, v, s):
        self.val = v
        self.sum = s
        self.dup = 1
        self.left = None
        self.right = None

        
        

# 2017.05.20
# Merge Sort cleaner version
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(nums):
            if len(nums) <= 1: return nums
            mid = len(nums) // 2
            left, right = sort(nums[:mid]), sort(nums[mid:])
            for i in xrange(len(nums) - 1, -1, -1):
                if not right or (left and left[-1][1] > right[-1][1]):
                    res[left[-1][0]] += len(right)
                    nums[i] = left.pop()
                else:
                    nums[i] = right.pop()
            return nums
        res = [ 0 for _ in xrange(len(nums)) ]
        sort(list(enumerate(nums)))
        return res

# 2017.05.20
# Merge Sort Template
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(nums, lo, hi):
            mid = (lo + hi) // 2
            if mid == lo: return
            sort(nums, lo, mid)
            sort(nums, mid, hi)
            cache = [ [] for _ in xrange(hi - lo)]
            i, k, cnt = mid, 0, 0
            for left in xrange(lo, mid):
                while i < hi and nums[left][1] > nums[i][1]:
                    cnt += 1
                    cache[k] = nums[i]
                    i, k = i + 1, k + 1
                res[nums[left][0]] += cnt   # Update res only loop finished
                cache[k] = nums[left]
                k += 1
            cache[k:] = nums[i:hi]
            nums[lo:hi] = cache
            #print(res)
            #print(nums[lo:hi], cache)
            
        res = [ 0 for _ in xrange(len(nums)) ]
        sort(list(enumerate(nums)), 0, len(nums))
        return res

# 2017.05.15
# Merge sort solution
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                # This section just rearrage enum from right to left so that right is the biggest
                for i in xrange(len(enum) - 1, -1, -1):  
                    if not right or (left and left[-1][1] > right[-1][1]):  # num left > num right
                        smaller[left[-1][0]] += len(right)  # update left res + 1
                        enum[i] = left.pop()                # left[-1] bigger
                    else:                               # right[-1] bigger
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


# 2017.5.15
# Naive n**2 TLE for the large case
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        n = len(nums)
        res = [ 0 for x in xrange(n)]
        
        for i in xrange(n):
            count = 0
            for j in xrange(i+1, n):
                if nums[i] > nums[j]:
                    count += 1
            res[i] = count
        return res
