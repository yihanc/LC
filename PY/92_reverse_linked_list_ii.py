# 92. Reverse Linked List II   QuestionEditorial Solution  My Submissions
# Total Accepted: 89134
# Total Submissions: 302344
# Difficulty: Medium
# Contributors: Admin
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Simple one-pass solution
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        for i in xrange(m-1):
            pre = pre.next
        
        print(pre.val)
        cur = pre.next
        then = cur.next
        print(n-m)
        for i in xrange(n-m):
            print("---")
            print(cur.val)
            print(then.val)
            cur.next = then.next
            then.next = pre.next
            pre.next = then
            then = cur.next
        
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)

    l1.next = l2
    l2.next = l3

    Solution().reverseBetween(l1, 1, 3)

# Too complicated..
class Solution2(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:     # m == n, return the same list
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        lastEnd = dummy
        
        while m > 1:
            lastEnd = lastEnd.next
            m -= 1
            n -= 1

        toReverseHead = lastEnd.next
        toReverseEnd = toReverseHead
        
        while n - m > 0:
            toReverseEnd = toReverseEnd.next
            n -= 1
            
        nextStart = toReverseEnd.next
        toReverseEnd.next = None
        
        reversedList = self.reverseList(toReverseHead, toReverseEnd)
        lastEnd.next = reversedList[0]
        reversedList[1].next = nextStart
        return dummy.next
        
    def reverseList(self, head, tail):
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return [tail, head]

