# 143. Reorder List   QuestionEditorial Solution  My Submissions
# Total Accepted: 78773
# Total Submissions: 323956
# Difficulty: Medium
# Contributors: Admin
# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2-> ...
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# 
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 12.08.2016 Rewrite. Better version
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return
    
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        # reverse
        pre, cur, nex = slow, slow.next, slow.next.next
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        l1, l2 = head, pre.next
        pre.next = None
        
        while l2:
            cur1, cur2 = l1, l2
            l1, l2 = l1.next, l2.next
            cur2.next = l1
            cur1.next = cur2
        
        return

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: # B1, if len <= 2, return
            return 
        
        # 1. Find 2nd half
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # 2. Reverse 2nd half
        pre, cur = slow, slow.next
        #print(pre.val, " ", cur.val, " ", cur.next.val)
        while cur.next:
            then = cur.next
            cur.next = then.next
            then.next = pre.next
            pre.next = then
        
        # 3. Reconstruct
        p1, p2 = head, pre.next
        pre.next = None         # Break p1 and p2 for easy looping.
        
        while p1 or p2:
            if p1:
                cur = p1
                p1 = p1.next
                cur.next = p2
            if p2:
                cur = p2
                p2 = p2.next
                cur.next = p1
            
        return
        
        
if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
#    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
#    n3.next = n4
    cur = n1
    while cur:
        print(cur.val)
        cur = cur.next

    print("-----start-------")
    Solution().reorderList(n1)

    print("-----finish-------")
    cur = n1
    while cur:
        print(cur.val)
        cur = cur.next
