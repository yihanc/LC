"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root: return node
        
        cur = root
        while cur:
            if node.val < cur.val:
                if not cur.left:
                    cur.left = node
                    return root
                cur = cur.left
            elif node.val > cur.val:
                if not cur.right:
                    cur.right = node
                    return root
                cur = cur.right
                
