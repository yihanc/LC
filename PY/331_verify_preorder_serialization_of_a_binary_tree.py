# 331. Verify Preorder Serialization of a Binary Tree Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 33342
# Total Submissions: 93443
# Difficulty: Medium
# Contributor: LeetCode
# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
# 
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
# 
# Example 2:
# "1,#"
# Return false
# 
# Example 3:
# "9,#,#,1"
# Return false

# 2017.05.13
# dietpepsi in out 
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        diff = 1
        nodes = preorder.split(',')
        for node in nodes:
            diff -= 1
            if diff < 0: return False
            if node != '#': diff += 2
        return diff == 0

# Another stack 
from collections import deque
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        d = deque()
        for node in preorder.split(','):
            while node == '#' and d and d[-1] == '#':
                #print(d)
                d.pop()
                if not d: return False
                d.pop()
            d.append(node)
        return d and d[-1] == '#'
