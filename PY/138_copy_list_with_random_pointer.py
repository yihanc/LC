# 138. Copy List with Random Pointer   QuestionEditorial Solution  My Submissions
# Total Accepted: 83720
# Total Submissions: 318414
# Difficulty: Hard
# Contributors: Admin
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# Subscribe to see which companies asked this question
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# 2018.03.22
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        dic = {}
        cur = head
        while cur:
            clone = RandomListNode(cur.label)
            dic[cur] = clone
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next: dic[cur].next = dic[cur.next]
            if cur.random: dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]

# 2017.04.04 Rewrite and shorter
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return
        dic = {}
        cur = head
        while cur:
            dic[cur] = RandomListNode(cur.label)
            cur = cur.next
        for k, v in dic.iteritems():
            if k.random: v.random = dic[k.random]
            if k.next: v.next = dic[k.next]
        return dic[head]

# Create node and mapping first
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        dic = {}
        cur = head
        while cur:                          # Step 1. Create all nodes. And bind dic
            node = RandomListNode(cur.label)
            dic[cur] = node
            cur = cur.next
        
        cur = head
        while cur:                          # Step 2. Update next and random
            if cur.next: dic[cur].next = dic[cur.next] 
            if cur.random: dic[cur].random = dic[cur.random]
            cur = cur.next
        
        return dic[head]    
        
