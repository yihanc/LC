# 234. Palindrome Linked List Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 91931
# Total Submissions: 287815
# Difficulty: Easy
# Contributors: Admin
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 2018.03.10
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        i, j = 0, len(res) - 1
        while i < j and res[i] == res[j]:
            i, j = i + 1, j - 1
        return False if i < j else True


# 2017.03.25 Better way
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        l2 = self.reverseList(slow.next)

        cur1, cur2 = head, l2
        while cur2:
            if cur1.val != cur2.val:
                return False
            
            cur1, cur2 = cur1.next, cur2.next
        return True
    
    def reverseList(self, head):
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = pre.next
        post = cur.next
        
        while post:
            cur.next = post.next
            post.next = pre.next
            pre.next = post
            post = cur.next
        
        return dummy.next
