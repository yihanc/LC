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


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
#    root.right = TreeNode(1)
    Solution().recoverTree(root)
    print(root.val)
    print(root.left.val)

