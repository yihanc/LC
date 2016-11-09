# 206. Reverse Linked List   QuestionEditorial Solution  My Submissions
# Total Accepted: 161075
# Total Submissions: 377427
# Difficulty: Easy
# Contributors: Admin
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        cur = pre.next
        next = cur.next
        
        while next:         # Reverse link list template
            cur.next = next.next
            next.next = pre.next
            pre.next = next
            next = cur.next
            
        return dummy.next
