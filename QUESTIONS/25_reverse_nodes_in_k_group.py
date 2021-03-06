# 25. Reverse Nodes in k-Group My Submissions QuestionEditorial Solution
# Total Accepted: 60525 Total Submissions: 217857 Difficulty: Hard
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# function to reverse a list
class Solution(object):
    def reverseListNode(self, head):
        if not head or not head.next: return head
        
        # Reverse List
        cur, nex, cur.next = head, head.next, None
        while nex:
            tmp = nex.next
            nex.next = cur
            cur = nex
            nex = tmp
        
        return [cur,head]

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1: return head
        
        dummyhead = ListNode(0)
        dummyhead.next = head
        start = end = dummyhead
        
        for i in xrange(k):
            if end: 
                end = end.next
            
        while end:
            endNext = end.next
            end.next = None         #disconnect and reverse
            rList = self.reverseListNode(start.next)
            start.next = rList[0]   #connect them back
            rList[1].next = endNext
            
            # Move pointers
            start = end = rList[1]
            for i in xrange(k):
                if end:
                    end = end.next
        
        return dummyhead.next

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        A = Solution().reverseKGroup(n1, 3)  

        print("A result:")
        while A:
            print(A.val)
            A = A.next

        b1 = ListNode(1)
        b2 = ListNode(2)
        b3 = ListNode(3)
        b4 = ListNode(4)
        b5 = ListNode(5)
        b3.next = b2
        b2.next = b1
        b1.next = b4
        b4.next = b5
        B = b3

        print("B result:")
        while B:
            print(B.val)
            B = B.next
        self.assertEqual(A, B)

if __name__ == "__main__":
    unittest.main()
