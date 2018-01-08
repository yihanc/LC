"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""



# 2018.1.1 Inorder Morris O(1)
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.cur = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return True if self.cur else False

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        res = None
        cur = self.cur
        while cur:
            if not cur.left:
                res = cur
                cur = cur.right
                break
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if pre.right != cur:
                    pre.right = cur
                    cur = cur.left
                else:
                    res = cur
                    pre.right = None
                    cur = cur.right
                    break
        self.cur = cur
        return res

