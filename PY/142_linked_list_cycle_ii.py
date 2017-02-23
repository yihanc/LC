# 142. Linked List Cycle II   QuestionEditorial Solution  My Submissions
# Total Accepted: 94212
# Total Submissions: 302168
# Difficulty: Medium
# Contributors: Admin
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# Note: Do not modify the linked list.
# 
# Follow up:
# Can you solve it without using extra space?
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 1. Same as detech cycle. 
# 2. Once slow == fast. Assign fast = head, once slow == fast again, return slow.
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    slow, fast = slow.next, fast.next
                return slow
        
        return None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
            
        if slow != fast:
            return None
        else:
            fast = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    print(Solution().detectCycle(n1).val)
