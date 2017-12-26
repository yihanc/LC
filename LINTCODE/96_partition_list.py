"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        l1dummy = ListNode(-1)
        l2dummy = ListNode(-1)
        l1, l2 = l1dummy, l2dummy
        
        cur = head
        while cur:
            if cur.val < x:
                l1.next = cur
                l1 = l1.next
                cur = cur.next
                l1.next = None
            else:
                l2.next = cur
                l2 = l2.next
                cur = cur.next
                l2.next = None
        
        l1.next = l2dummy.next
        return l1dummy.next
