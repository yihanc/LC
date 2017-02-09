# 117. Populating Next Right Pointers in Each Node II  QuestionEditorial Solution  My Submissions
# Total Accepted: 71555
# Total Submissions: 215749
# Difficulty: Hard
# Follow up for problem "Populating Next Right Pointers in Each Node".
# 
# What if the given tree could be any binary tree? Would your previous solution still work?
# 
# Note:
# 
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# Subscribe to see which companies asked this question117. Populating Next Right Pointers in Each Node II  QuestionEditorial Solution  My Submissions
# Total Accepted: 71555
# Total Submissions: 215749
# Difficulty: Hard
# Follow up for problem "Populating Next Right Pointers in Each Node".
# 
# What if the given tree could be any binary tree? Would your previous solution still work?
# 
# Note:
# 
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# Subscribe to see which companies asked this question

# 1.1.2017 Same solution as 116. Level Order traversal.
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        d = deque()
        d.append([root, 1])
        while d:
            cur, dep = d.pop()
            
            if d and d[-1][1] == dep:
                cur.next = d[-1][0]
            
            if cur.left: d.appendleft([cur.left, dep + 1])
            if cur.right: d.appendleft([cur.right, dep + 1])
        
        return

# 12.03.2016 Rewrite. less code
# nextlvl and first pointer. If found, update

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return 
        
        first = None
        
        curlvl, nextlvl = root, None
        while curlvl:
            cur = curlvl
            while cur:
                if cur.left: 
                    if not nextlvl: nextlvl = cur.left
                    if not first: 
                        first = cur.left
                    else:
                        first.next = cur.left
                        first = cur.left
                if cur.right:
                    if not nextlvl: nextlvl = cur.right
                    if not first: 
                        first = cur.right
                    else:
                        first.next = cur.right
                        first = cur.right
                
                cur = cur.next
            
            curlvl = nextlvl
            nextlvl = None
            first = None
        
        return 


# Steps:
# "nextHead" to record next level head.
# "start" to record last node to connect on the same level
# for each loop. cur = cur.next or cur = nextHead if not cur.next
# then 1. Set nextHead if not set 2. Connect nodes

# Iterative. O(1) space
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        cur, nextHead, start = root, None, None
        
        # When to stop? cur = nextHead = None 
        while cur:
            # Setting curHead
            if not nextHead:
                if cur.left: 
                    nextHead = cur.left
                elif cur.right:
                    nextHead = cur.right
                else:
                    pass

            # Connecting
            if cur.left and cur.right:
                if start:
                    start.next = cur.left
                cur.left.next = cur.right
                start = cur.right 
            elif cur.left:
                if start:
                    start.next = cur.left
                start = cur.left
            elif cur.right:
                if start:
                    start.next = cur.right
                start = cur.right
            else:
                pass

            # Passing to next level
            if cur.next:    # Same level
                cur = cur.next  
            else:           # to the next level
                cur = nextHead
                nextHead, start = None, None
