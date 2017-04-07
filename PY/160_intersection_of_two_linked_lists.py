# 160. Intersection of Two Linked Lists   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 102835
# Total Submissions: 342701
# Difficulty: Easy
# Contributors: Admin
# Write a program to find the node at which the intersection of two singly linked lists begins.
# 
# 
# For example, the following two linked lists:
# 
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
# 
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Better concise solution. gc.collect() can be commented.
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        gc.collect()
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# 2017.04.07 Self wrote Tedious
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2, f1, f2 = headA, headB, False, False
        while p1 and p2 and p1 != p2:
            p1, p2 = p1.next, p2.next
            if not p1 and not f1: 
                p1, f1 = headB, True
            if not p2 and not f2: 
                p2, f2 = headA, True
        return None if p1 != p2 or not p1 or not p2 else p1

