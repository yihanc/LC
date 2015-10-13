# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    size = 0

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return [[]]
        
        res = []
        self.generateTreesHelper(1, n, res, n, None)
        return res
    
    def generateTreesHelper(self, start, end, res, target, head):
        """
        :type nums: List[int]
        :type res: List[TreeNode]
        :rtype: TreeNode
        """

        if start > end:
            return None

        
        for i in range(start, end+1):
##            print ("----------")
            cur = TreeNode(i)
            if self.size == 0:
                head = cur
            self.size = self.size + 1
            print (str(i) + "               Size: " + str(self.size))
            if self.size == target:
                print ("-------")
                res.append(head)
            cur.left = self.generateTreesHelper(start, i-1, res, target, head)
            cur.right = self.generateTreesHelper(i+1, end, res, target, head)
            print ("Calling")
            self.size = self.size - 1


sol = Solution()
## sol.generateTrees(0)
## print ("*************************")
## sol.generateTrees(1)
## print ("*************************")
## sol.generateTrees(2)
## print ("*************************")
sol.generateTrees(3)
## print ("*************************")
## sol.generateTrees(4)

