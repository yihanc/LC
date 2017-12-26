"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head: return
        mp = {}
        cur = head
        while cur:
            mp[cur] = RandomListNode(cur.val)
            cur = cur.next
        
        for k, v in mp.iteritems():
            if k.random: v.random = mp[k.random]
            if k.next: v.next = mp[k.next]
        return mp[head]
