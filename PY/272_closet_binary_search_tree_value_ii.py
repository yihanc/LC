# 272. Closest Binary Search Tree Value II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 15854
# Total Submissions: 41240
# Difficulty: Hard
# Contributor: LeetCode
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
# 
# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# 2017.05.21
# inorder + k size []
# Faster

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            # abs(target - node.val) will become smaller then bigger. 
            # We stop when 
            if len(res) == k:
                if abs(node.val - target) <= abs(res[0] - target):
                    del res[0]
                else:
                    return
            res.append(node.val)
            dfs(node.right)
            
        res = []
        dfs(root)
        return res


# 2017.05.21
# inorder traversal + heapq o(n)
# Slower 142ms
from heapq import *
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            heappush(hq, [abs(target - node.val), node.val])
            dfs(node.right)

        hq = []
        dfs(root)
        res = []
        while k > 0:
            res.append(heappop(hq)[1])
            k -= 1
        return res


