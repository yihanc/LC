# 23. Merge k Sorted Lists My Submissions QuestionEditorial Solution
# Total Accepted: 87612 Total Submissions: 370428 Difficulty: Hard
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = Nonsa


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
