# 581. Shortest Unsorted Continuous Subarray Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 4554
# Total Submissions: 15094
# Difficulty: Easy
# Contributors:
# love_Fawn
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

# 2017.05.26
# Scan twice find begin and end
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = float('-inf')
        end = -2
        for i in xrange(len(nums)):
            mx = max(mx, nums[i])
            if nums[i] < mx: end = i

        mi = float('inf')
        start = -1
        for i in xrange(len(nums) - 1, -1, -1):
            mi = min(mi, nums[i])
            if nums[i] > mi: start = i

        return end - start + 1

# 2017.05.26
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            dic[node.val] = dic.get(node.val, 0) + 1
            maxfre[0] = max(maxfre[0], dic[node.val])
            dfs(node.right)
        
        dic = {}
        maxfre = [0]
        dfs(root)
        res = []
        for k, v in dic.iteritems():
            if v == maxfre[0]: res.append(k)
        return res
