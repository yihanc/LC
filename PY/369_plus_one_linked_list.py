# 369. Plus One Linked List Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14019
# Total Submissions: 25926
# Difficulty: Medium
# Contributor: LeetCode
# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of the list.
# 
# Example:
# Input:
# 1->2->3
# 
# Output:
# 1->2->4

# 2017.05.29
# Recursive

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        carry = self.plusOneHelper(head)
        if carry == 1:
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        return head
            
    
    def plusOneHelper(self, head):
        if not head: return 0
        carry = 0
        if not head.next: 
            head.val += 1
        else:
            carry = self.plusOneHelper(head.next)
            
        head.val += carry
        if head.val == 10:
            head.val = 0
            return 1
        else:
            return 0
        
        
        
