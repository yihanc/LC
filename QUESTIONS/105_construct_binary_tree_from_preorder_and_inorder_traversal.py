#105. Construct Binary Tree from Preorder and Inorder Traversal QuestionEditorial Solution  My Submissions
#Total Accepted: 76610 Total Submissions: 255209 Difficulty: Medium
#Given preorder and inorder traversal of a tree, construct the binary tree.
#
#Note:
#You may assume that duplicates do not exist in the tree.
#
#Subscribe to see which companies asked this question
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.right = None

# Watch out the start/END value for preorder !
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeHelper(preorder, inorder, 0, len(preorder), 0, len(inorder))
    
    def buildTreeHelper(self, preorder, inorder, preS, preE, inS, inE):
        if preS >= preE or inS >= inE:
            return None
        
        root = TreeNode(preorder[preS])
        i = inorder.index(root.val)
        root.left = self.buildTreeHelper(preorder, inorder, preS+1, preS+1+(i-inS), inS, i)
        root.right = self.buildTreeHelper(preorder, inorder, preS+1+(i-inS), preE, i+1, inE)
        return root

if __name__ == "__main__":
    pre = [1, 2]
    ino = [2, 1]
    Solution().buildTree(pre, ino)

exit

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """


## 1 This solution is getting MLE
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
