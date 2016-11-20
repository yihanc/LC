# 109. Convert Sorted List to Binary Search Tree   QuestionEditorial Solution  My Submissions
# Total Accepted: 87044
# Total Submissions: 269879
# Difficulty: Medium
# Contributors: Admin
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
            
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        cur = slow.next
        rightList = slow.next.next
        slow.next = None

        curNode = TreeNode(cur.val)
        curNode.left = self.sortedListToBST(head)
        curNode.right = self.sortedListToBST(rightList)
        
        return curNode
        

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(3)
    l1.next = l2
    Solution().sortedListToBST(l1)
