"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        def _dfs(node):
            if not node: 
                res.append("#")
                return
            res.append(str(node.val))
            _dfs(node.left)
            _dfs(node.right)
        
        if not root: return ""
        res = []
        _dfs(root)
        return " ".join(res)
        

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        def _dfs():
            if not A: return None
            val = A.pop()
            if val == "#": return None
            node = TreeNode(int(val))
            node.left = _dfs()
            node.right = _dfs()
            return node
            
        A = data.split()[::-1]
        return _dfs()

        
        
