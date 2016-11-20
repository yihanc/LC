# 147. Insertion Sort List   QuestionEditorial Solution  My Submissions
# Total Accepted: 86360
# Total Submissions: 275419
# Difficulty: Medium
# Contributors: Admin
# Sort a linked list using insertion sort.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Better and clear solution. Two loop.
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        dummy = ListNode(-1)
        pre = dummy
        
        cur = head
        while cur:
            tmp = cur.next
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy    
            cur = tmp
        
        return dummy.next

                
if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    Solution().insertionSortList

# TLE in really big case
# class Solution(object):
#     def insertionSortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head or not head.next:
#             return head
#         
#         p1 = head
#         dummy = ListNode(-1)
# 
#         while p1:
#             p2 = dummy
#             while p2:
#                 if not p2.next:             # If > all p2, append end.
#                     tmp = p1
#                     p1 = p1.next
#                     tmp.next = None
#                     p2.next = tmp
#                     break
#             
#                 if p1.val <= p2.next.val:   # if <= p2.next, insert p2, XX, p2.next
#                     tmp = p1
#                     p1 = p1.next
#                     tmp.next = p2.next
#                     p2.next = tmp
#                     break
#                 p2 = p2.next
# 
#         return dummy.next
#         
