class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print("--------", root.val)
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        leftHeight, rightHeight = 0, 0
        
        if root.left:
            print("calling left of ", root.left.val)
            leftHeight = self.maxDepth(root.left)
        if root.right:
            print("calling right of ", root.right.val)
            rightHeight = self.maxDepth(root.right)
        
        return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    A.left = B
    A.right = D
    B.left = C
    print(Solution().maxDepth(A))
    
