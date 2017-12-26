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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def mergeLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        if l1: cur.next = l1
        else: cur.next = l2
        return dummy.next
        
    def sortList(self, head):
        # write your code here
        if not head or not head.next: return head
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None
        
        left = self.sortList(l1)
        right = self.sortList(l2)
        
        return self.mergeLists(left, right)
        
