
# 12.30.2017
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        if n >= 2: return self.merge2Lists(self.mergeKLists(lists[:n//2]), 
            self.mergeKLists(lists[n//2:]))
        
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if not l1: cur.next = l2
        else: cur.next = l1
        return dummy.next
        


