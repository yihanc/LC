# 146. LRU Cache   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 101493 Total Submissions: 636611 Difficulty: Hard Contributors: Admin
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# Subscribe to see which companies asked this question
# 
# 

# 2017.06.01 
# Doublelist + Dictionary
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxcap = capacity
        self.dic = {}   #Holds key -> DD node
        self.ddHead = DoubleListNode(-1, -1)
        self.ddTail = DoubleListNode(-1, -1)
        self.ddHead.next = self.ddTail
        self.ddTail.prev = self.ddHead

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.ddRemove(node)
            self.ddAppend(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dic:
            node = DoubleListNode(key, value)
            if self.maxcap == len(self.dic) # remoe old
                del self.dic[self.ddHead.next.key]
                self.ddRemove(self.ddHead.next)
            self.dic[key] = node
            self.ddAppend(node)
        else:
            node = self.dic[key]
            node.value = value
            self.ddRemove(node)
            self.ddAppend(node)

    def ddRemove(self, node):
        n1, n2 = node.prev, node.next
        n1.next, n2.prev = n2, n1
        node.prev, node.next = None, None
    
    def ddAppend(self, node):
        n1, n2 = self.ddTail.prev, self.ddTail
        n1.next, n2.prev = node, node
        node,prev, node.next = n1, n2

        
class DoubleListNode(object):
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


            

if __name__ == "__main__":
    node1 = DLinkedNode("A", "A")
    node2 = DLinkedNode("B", "B")
    node1.post = node2
    node2.pre = node1
    node3 = DLinkedNode("C", "C")
    node4 = DLinkedNode("D", "D")

    node1.add(node3)
    node1.add(node4)

#    node3.remove()
#    node4.remove()

#    print(node2.value)
#    node2.popTail()
#    node3.popTail()
    node1.moveToHead(node3)

    cur = node1
    while cur:
        print(cur.key, cur.value, cur, cur.pre, cur.post)
        cur = cur.post


