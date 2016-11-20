# 145. Binary Tree Postorder Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 98882 Total Submissions: 276642 Difficulty: Hard
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative using deque
# Use one variable to check last node visited

# Iterative using one stack
# 1.1 Create an empty stack
# 2.1 Do following while root is not NULL
#     a) Push root's right child and then root to stack.
#     b) Set root as root's left child.
# 2.2 Pop an item from stack and set it as root.
#     a) If the popped item has a right child and the right child 
#        is at top of stack, then remove the right child from stack,
#        push the root back and set root as root's right child.
#     b) Else print root's data and set root as NULL.
# 2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        d = deque()
        cur = root
        while d or cur:
            if cur:
                if cur.right:
                    d.append(cur.right)
                d.append(cur)
                cur = cur.left
            else:
                cur = d.pop()
                if d and cur.right and cur.right == d[-1]:
                    d.pop()
                    d.append(cur)
                    cur = cur.right
                else:
                    res.append(cur.val)
                    cur = None
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(Solution().postorderTraversal(root))
    

exit







# Iterative two stacks (preorder)
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        d1, d2 = deque(), deque()
        d1.append(root)
        while d1:
            cur = d1.pop()
            d2.append(cur)
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s2.append(cur.right)

        while d2:
            cur = d2.pop()
            res.append(cur.val)

        return res
        

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)













from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, d = [], deque()
        cur = root
        lastNodeVisit = None
        while d or cur:
            if cur:
                d.append(cur)
                cur = cur.left
            else:
                peekNode = d.pop()
                if peekNode.right and peekNode.right != lastNodeVisit:
                    d.append(peekNode)
                    cur = peekNode.right
                else:
                    res.append(peekNode.val)
                    lastNodeVisit = peekNode
        return res


# Iterative using deque and isVisit
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, isVisit = [], {}
        d = deque()
        d.append(root)
        while d:
            cur = d.pop()   
            d.append(cur)   # no peek in deque
            if cur.right and cur.right not in isVisit: 
                d.append(cur.right)
            if cur.left and cur.left not in isVisit: 
                d.append(cur.left)
            if (not cur.right or cur.right in isVisit ) and (not cur.left or cur.left in isVisit):
                cur = d.pop()
                res.append(cur.val)
                isVisit[cur] = True
        
        return res

# Recursive
class Solution(object):
    def dfs(self, root, res):
        if not root: return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
