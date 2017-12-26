# Problem
# Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.
# 思路
# Delete node 有三种情况
# 因为要delete,在find这个node的过程中要保留一个parent的变量
# leaf node
# 删掉这个node，把parent对这个node的reference设为null
# Node with only one child
# delete the node,把parent对node的reference link到node的child
# Node with 2 children
# find the minimum node of right subtree
# replace the value of found node
# delete the old duplicate node(case 1/2, cause minimum node should not have left child)


