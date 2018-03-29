# 173. Binary Search Tree Iterator Add to List
# Description  Submission  Solutions
# Total Accepted: 79512
# Total Submissions: 200401
# Difficulty: Medium
# Contributors: Admin
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2018.03.10 stack traversal
'''
**hasNext() should be IDEMPOTENT**

I have seen different solutions passing the OJ, however, some of the solutions are questionable if you are changing states in the hasNext() call.

Why? In reality, you would have no controls of how many times hasNext() being called and it should produce the same results, which we called "idempotency". Although those solutions can pass Leetcode OJ, that's because OJ is always calling hasNext() exactly once before calling next(). Your solution might be questioned during the real interview.

So, how do we achieve "idempotency" in hasNext()?

**General Solution for Iterator**
An Iterator is nothing but contains a hasNext(), next() method and a constructor to initiate the state.

Before implementing the iterator, we should know how to traverse it. In this case, it is obviously inorder traversal. Then, we can implement the iterator following below approach:

* **init()** - the init() method should only do two things:
    * Initiate pointer and data structure states
    * Move your pointer to the first element
* **hasNext()** - The hasNext() method should do nothing but checking if the value of current pointer is valid or not, no states should be changed.
* **next()**- The next() should move the pointer to the next available after outputing the current value. It can be achieved in 3 steps.
    * Save the current pointer value
    * Move the current pointer to the next value
    * Output the saved value

By Shiyan
'''


from collections import deque
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root
        self.d = deque()
        while self.cur or self.d:
            if self.cur:
                self.d.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.d.pop()
                break

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.cur else False
        

    def next(self):
        """
        :rtype: int
        """
        ans = self.cur
        self.cur = self.cur.right
        while self.cur or self.d:
            if self.cur:
                self.d.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.d.pop()
                break
        return ans.val



from collections import deque

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

