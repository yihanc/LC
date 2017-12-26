"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root: return []
        res = []

        cur = root
        while cur:
            print(res)
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    cur = cur.right
        return res
