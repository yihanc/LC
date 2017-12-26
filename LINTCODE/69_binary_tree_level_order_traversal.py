"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root: return []
        res = []
        d = deque()
        d.append([0, root])
        while d:
            dep, cur = d.pop()
            print(dep, cur.val)
            while len(res) <= dep:
                res.append([])
            res[dep].append(cur.val)
            if cur.left: d.appendleft([dep + 1, cur.left])
            if cur.right: d.appendleft([dep + 1, cur.right])
        return res
            
