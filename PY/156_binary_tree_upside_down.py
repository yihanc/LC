# [1] 156 Binary Tree Upside Down
# 
# 38.7%   Medium
# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
# 
# For example:
# Given a binary tree {1,2,3,4,5},
#     1
#    / \
#   2   3
#  / \
# 4  5
# 
# return the root of the binary tree [4,5,2,#,#,3,1].
#     4
#    / \
#   5   2
#  / \
# 3   1
from collectionsi import deque

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Soltuion(object):
    def bstUpSideDown(self, root):
        if not root: return root
        d = deque()
        cur = root
        while cur.left:
            d.append(cur)
            cur = cur.left
        newroot = cur
        while d:
            parent = d.pop()
            cur.left = parent.right
            

