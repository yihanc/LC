"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: the List
    @param: k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head or not head.next or k == 0: return head
        dummy = ListNode(-1)
        dummy.next = head
        
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        k = k % count
        if k == 0: return head
        
        fast = dummy
        while k > 0:
            fast = fast.next
            k -= 1
        
        slow = dummy
        while fast.next:
            slow, fast = slow.next, fast.next
        
        l2 = slow.next
        slow.next = None
        fast.next = head
        dummy.next = l2
        return dummy.next
        
        
        

