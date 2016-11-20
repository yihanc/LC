# 19. Remove Nth Node From End of List My Submissions QuestionEditorial Solution
# Total Accepted: 111155 Total Submissions: 372725 Difficulty: Easy
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 11.19.2016
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        pre, fast = dummy, dummy
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast.next:
            pre, fast = pre.next, fast.next
            
        pre.next = pre.next.next
        return dummy.next

# Slow Fast Pointers
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        
        slow = fast = dummyhead
        while n > -1:
            fast = fast.next
            n -= 1
            
        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummyhead.next
        
