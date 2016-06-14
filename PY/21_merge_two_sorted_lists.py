# 21. Merge Two Sorted Lists My Submissions QuestionEditorial Solution
# Total Accepted: 130341 Total Submissions: 364494 Difficulty: Easy
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head

        while l1 or l2:
            # l1 or l2 is None
            if not l1:
                cur.next = l2
                return head.next
            elif not l2:
                cur.next = l1
                return head.next
            # l1 and l2 have value
            elif l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        return head.next
