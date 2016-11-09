# 61. Rotate List   QuestionEditorial Solution  My Submissions
# Total Accepted: 87391
# Total Submissions: 366738
# Difficulty: Medium
# Contributors: Admin
# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: 
            return None
            
        dummy = ListNode(-1)
        dummy.next = head
        
        count = 0
        while head:
            head = head.next
            count += 1

        k = k % count       # TLE for case k is very large
        if k == 0:
            return dummy.next

        fast = dummy
        while k > 0:
            fast = fast.next
            k -= 1
    
        slow = dummy
        while fast.next:
            slow, fast = slow.next, fast.next
        
        pivot = slow.next
        slow.next = None
        fast.next = dummy.next
        return pivot
