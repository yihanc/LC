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

# 12.10.2016, Merge sort. Space is logn
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        slow, fast = dummy, dummy.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        l2 = slow.next
        slow.next = None
        
        ll = self.sortList(head)
        rr = self.sortList(l2)
        
        return self.merge(ll, rr)
    
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        
        while l1 or l2:
            if l1 and not l2:
                cur.next = l1
                break
            if l2 and not l1:
                cur.next = l2
                break

            if l1.val < l2.val:
                tmp = l1.next
                l1.next = None
                cur.next = l1
                cur, l1 = cur.next, tmp
            else:
                tmp = l2.next
                l2.next = None
                cur.next = l2
                cur, l2 = cur.next, tmp
        
        return dummy.next


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

