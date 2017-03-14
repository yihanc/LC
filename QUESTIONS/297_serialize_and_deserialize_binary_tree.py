# 297. Serialize and Deserialize Binary Tree Add to List
# Description  Submission  Solutions
# Total Accepted: 51258
# Total Submissions: 159072
# Difficulty: Hard
# Contributors: Admin
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# 
# For example, you may serialize the following tree
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
# 
# Credits:
# Special thanks to @Louis1992 for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# One clean solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

if __name__ == "__main__":
    ns = []
    for i in xrange(5):
        ns.append(TreeNode(i))
    
    ns[0].left = ns[1]
    ns[0].right = ns[2]
    ns[2].left = ns[3]
    ns[2].right = ns[4]
    
    print(Codec().serialize(ns[0]))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
