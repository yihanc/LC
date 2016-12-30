# 83. Remove Duplicates from Sorted List   QuestionEditorial Solution  My Submissions
# Total Accepted: 147717
# Total Submissions: 384802
# Difficulty: Easy
# Contributors: Admin
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 12.28.2016 Rewrite. No dummy

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:        
            return None
        cur = head
        while cur.next: 
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return head
