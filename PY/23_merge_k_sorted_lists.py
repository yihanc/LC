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

# 11.19.2016
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0: 
            return None
            
        if n == 1: 
            return lists[0]
            
        half_len = (n + 1) // 2
        l1 = self.mergeKLists(lists[:half_len])
        l2 = self.mergeKLists(lists[half_len:])
        return self.mergeTwoLists(l1, l2)
        
    
    def mergeTwoLists(self, l1, l2):        # Time l1 + l2
        dummy = ListNode(-1)
        cur = dummy
        while l1 or l2:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break
            
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
            cur.next = None
                
        return dummy.next

# Merge Sort

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(0)
        cur = dummyHead
        
        while l1 or l2:
            # l1 or l2 is empty
            if not l1:
                cur.next = l2
                return dummyHead.next
            elif not l2:
                cur.next = l1
                return dummyHead.next
            
            # l1 and l2 have value
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return dummyHead.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        n = len(lists)
        if n == 1: return lists[0]
        if n == 2: 
            return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[:n//2]), self.mergeKLists(lists[n//2:]))
