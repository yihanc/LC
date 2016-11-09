# 86. Partition List   QuestionEditorial Solution  My Submissions
# Total Accepted: 81593
# Total Submissions: 262036
# Difficulty: Medium
# Contributors: Admin
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        end = head      # Find end ele
        while end.next:
            end = end.next

        curEnd = end
        isEnd = False   # Where to stop
        while cur and cur.next and not isEnd:
            if cur.next == end:
                isEnd = True
                
            if cur.next.val >= x:
                curEnd.next = cur.next
                curEnd = curEnd.next
                cur.next = cur.next.next
                curEnd.next = None
            else:
                cur = cur.next
        return dummy.next
