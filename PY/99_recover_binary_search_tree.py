# 99. Recover Binary Search Tree  QuestionEditorial Solution  My Submissions
# Total Accepted: 60075
# Total Submissions: 215046
# Difficulty: Hard
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 12.31.2016 Rewrite Morris
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        cur = root
        first, second = None, None
        last = None
        while cur:
            if not cur.left:
                # do something
                if last and cur.val <= last.val:
                   if not first: first = last
                   second = cur
                last = cur
                
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right != cur:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    # do something
                    if last and cur.val <= last.val:
                        if not first: first = last
                        second = cur
                    last = cur
                    
                    cur = cur.right

        if first and second:
            first.val, second.val = second.val, first.val
        return 

# 12.31.2016 Rewrite Recursive
class Solution(object):
#    res = [None, None]         # Why bug if res outside?? See https://leetcode.com/faq/#different-output
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = [None, None]
        prev = [None]           # Has to be a mutable object to be passed in function
        self.recoverTreeHelper(root, res, prev)
        if res[0] and res[1]:
            res[0].val, res[1].val = res[1].val, res[0].val
        return 
        
    def recoverTreeHelper(self, root, res, prev):
        if not root: return
    
        self.recoverTreeHelper(root.left, res, prev)
        
        if prev[0] != None and root.val <= prev[0].val:
            if res[0] == None: 
                res[0] = prev[0]
            res[1] = root
                
        prev[0] = root
        self.recoverTreeHelper(root.right, res, prev)
        return

# inorder traversal
# Iter O(1)
# Note if passing first,second,last in parameters, they won't got changed
# See stackoverflow python pass by reference explainantion

class Solution(object):
    first, second = None, None
    last = None
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if not cur.left:
                self.process(cur)
                cur = cur.right
            else:
                prev = cur.left

                while prev.right and prev.right != cur:
                    prev = prev.right

                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    self.process(cur)
                    cur = cur.right

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

    def process(self, root):
        if self.last and self.last.val > root.val:
            if not self.first:
                self.first = self.last
            self.second = root
        self.last = root
        

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    Solution().recoverTree(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)

exit


# Recursive.
class Solution2(object):
    prev = None
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = [None, None]
        self.traverse(root, res)
        if res[0] and res[1]:
            res[0].val, res[1].val = res[1].val, res[0].val
    
    def traverse(self, root, res):
        if not root:
            return 
        
        self.traverse(root.left, res)
        
        if self.prev and self.prev.val >= root.val:
            if not res[0]:
                res[0] = self.prev
            res[1] = root

        self.prev = root
        self.traverse(root.right, res)
