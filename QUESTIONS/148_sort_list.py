# 148. Sort List   QuestionEditorial Solution  My Submissions
# Total Accepted: 87550
# Total Submissions: 325686
# Difficulty: Medium
# Contributors: Admin
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## This is o(n) space.
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        nums.sort()
        dummy = ListNode(-1)
        pre = dummy
        for num in nums:
            node = ListNode(num)
            pre.next = node
            pre = node
        return dummy.next

