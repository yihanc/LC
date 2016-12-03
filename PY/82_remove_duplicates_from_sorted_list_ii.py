# 82. Remove Duplicates from Sorted List II   QuestionEditorial Solution  My Submission/^
# Total Accepted: 89550
# Total Submissions: 316449
# Difficulty: Medium
# Contributors: Admin
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 11.29.2016 Rewrite
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode("_")
        dummy.next = head
        
        pre = dummy
        while pre.next and pre.next.next:
            if pre.next.val == pre.next.next.val:
                cur = pre.next
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
        
        return dummy.next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur and cur.next and cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
                continue
            
            while cur.next.next and cur.next.val == cur.next.next.val:
                cur.next.next = cur.next.next.next
            cur.next = cur.next.next

        return dummy.next


if __name__ == "__main__":
    #A = [1,2,3,3,4,4,5]
    A = [1,1,1,2,3]
    B = []
    for val in A:
        B.append(ListNode(val))

    for i in xrange(len(B)-1):
        B[i].next = B[i+1]

    cur = B[0]
    while cur:
        print(cur.val)
        cur = cur.next
    print("------ START ------")

    res = Solution().deleteDuplicates(B[0])
    cur = res
    while cur:
        print(cur.val)
        cur = cur.next
