# 174. Remove Nth Node From End of List 
# Given a linked list, remove the nth node from the end of list and return its head.
# 
#  Notice
# The minimum number of nodes in list is n.
# 
# Have you met this question in a real interview? Yes
# Example
# Given linked list: 1->2->3->4->5->null, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5->null.

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head or n == 0: return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while n > 0:
            cur = cur.next
            n -= 1
        cur = cur.next
        pre = dummy
        
        while cur:
            cur, pre = cur.next, pre.next
        
        pre.next = pre.next.next
        return dummy.next
        
