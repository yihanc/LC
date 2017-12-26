"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        l1 = dummy.next
        cur = slow.next
        l2 = slow.next.next
        slow.next = None
        
        node = TreeNode(cur.val)
        node.left = self.sortedListToBST(l1)
        node.right = self.sortedListToBST(l2)
        return node
