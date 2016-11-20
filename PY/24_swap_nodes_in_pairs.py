# 24. Swap Nodes in Pairs My Submissions QuestionEditorial Solution
# Total Accepted: 100177 Total Submissions: 282334 Difficulty: Easy
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 11.19.2016 Reverse Template
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            # Swap Two nodes
            cur = pre.next
            then = cur.next
            cur.next = then.next
            then.next = pre.next
            pre.next = then
            pre = cur
        
        return dummy.next

class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        cur = dummyhead
        
        # Loop when next two nodes
        while cur.next and cur.next.next:
            n1, n2 = cur.next, cur.next.next
            n1.next = n2.next
            n2.next = n1
            cur.next = n2
            cur = cur.next.next
            
        return dummyhead.next
