# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return list(self.gen_trees(range(1,n+1)))

        
    def gen_trees(self, A):
        if A == []:
            yield None
            return

        for i in range(len(A)):
            for left in self.gen_trees(A[:i]):
                for right in self.gen_trees(A[i+1:]):
                    root = TreeNode(A[i])
                    root.left, root.right = left, right
                    yield root
                    

            
