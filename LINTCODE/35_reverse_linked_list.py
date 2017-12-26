"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur, post = dummy, head, head.next
        
        while cur.next:
            cur.next = post.next
            post.next = pre.next
            pre.next = post
            post = cur.next
        return dummy.next
