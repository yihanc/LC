# Problem
# Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.
# 思路
# Delete node 有三种情况
# 因为要delete,在find这个node的过程中要保留一个parent的变量
# leaf node
# 删掉这个node，把parent对这个node的reference设为null
# Node with only one child
# delete the node,把parent对node的reference link到node的child
# Node with 2 children
# find the minimum node of right subtree
# replace the value of found node
# delete the old duplicate node(case 1/2, cause minimum node should not have left child)


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
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root: return None
        
        dummy = TreeNode(float('inf'))
        dummy.left = root
        
        p, target = self._searchValue(dummy, value)
        if not target: return root
        
        if not target.left and not target.right:
            # Leaf node
            if p.left == target: 
                p.left = None
            else: 
                p.right = None
        elif not target.left and target.right:
            # Only right child
            if p.left == target: 
                p.left = target.right
            else: 
                p.right = target.right
        elif not target.right and target.left:
            # Only Left Child
            if p.left == target: 
                p.left = target.left
            else: 
                p.right = target.right
        else:
            # Two children
            minParent, minNode = self.findRightMinimum(target.right)
            if minParent.left == minNode:
                minParent.left = None
            else:
                minParent.right = None
            target.val = minNode.val
        return dummy.left


    def searchValue(self, root, value):
        p = root
        while p and p.val != value:
            if value > p.val:
                if p.right and p.right.val == value:
                    return p, p.right
                p = p.right
            elif value < p.val:
                if p.left and p.left.val == value:
                    return p, p.left
                p = p.left
            else:
                raise Exception("You should not reach here!")
        return p, None
    
    
    def findRightMinimum(self, root):
        parent = None
        while root.left:
            parent = root
            root = root.left
        return parent, root
            
