"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head or not head.next or not head.next.next: return head
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        l1 = head
        
        # reverse list 2
        pre, cur, post = slow, slow.next, slow.next.next
        while post:
            cur.next = post.next
            post.next = pre.next
            pre.next = post
            post = cur.next
        
        # Reorder
        l2 = pre.next
        pre.next = None
        
        l3 = ListNode(-1)
        cur = l3
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            cur.next = l2
            l2 = l2.next
            cur = cur.next
            
        if l1: cur.next = l1
        return l3

