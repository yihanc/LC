# 141. Linked List Cycle  QuestionEditorial Solution  My Submissions
# Total Accepted: 134530
# Total Submissions: 371666
# Difficulty: Easy
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow, fast = head, head
        
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
