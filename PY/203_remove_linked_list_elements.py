# 203. Remove Linked List Elements Add to List
# Description  Submission  Solutions
# Total Accepted: 99959
# Total Submissions: 319856
# Difficulty: Easy
# Contributors: Admin
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
                continue
            pre = pre.next
        return dummy.next
        

