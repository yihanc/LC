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

# 2017.02.24 Rewrite
# 1. Use dd for o(1). Initiate ddHead(LeastRecent), ddTail(MostRecent), mp{}, cap 
# 2. Get(). If in map update node to Tail and not in map.
# 3. Put().
# 3.1 If in map update value and move tail.
# 3.2 If not in map. If max cap, remove head.next first, add to tail

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxCap = capacity
        self.mp = {}
        self.ddHead = DoubleListNode(False, False)
        self.ddTail = DoubleListNode(False, False)
        self.ddHead.next = self.ddTail
        self.ddTail.prev = self.ddHead

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mp:
            self.ddRemove(self.mp[key])
            self.ddAddToTail(self.mp[key])
            return self.mp[key].value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        kv = DoubleListNode(key, value)
        if key in self.mp:
            self.mp[key].value = value
            self.ddRemove(self.mp[key])
            self.ddAddToTail(self.mp[key])
        else:
            if len(self.mp) == self.maxCap:
                tbdNode = self.ddHead.next
                self.ddRemove(tbdNode)
                del self.mp[tbdNode.key]
            self.ddAddToTail(kv)
            self.mp[key] = kv
            
    def ddRemove(self, node):
        """
        :type node: DoubleListNode
        """
        prevNode = node.prev
        postNode = node.next
        prevNode.next = postNode
        postNode.prev = prevNode
        
    def ddAddToTail(self, node):
        """
        :type node: DoubleListNode
        """
        tailPrev = self.ddTail.prev
        tailPrev.next = node
        node.next = self.ddTail
        self.ddTail.prev = node
        node.prev = tailPrev
        

class DoubleListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None




#######
class DLinkedNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

    def add(self, node):        # Add after current node
        node.pre, node.post = self, self.post
        self.post, node.post.pre = node, node

    def remove(self):
        pre = self.pre if self.pre else None
        post = self.post if self.post else None
        if pre: pre.post = post
        if post: post.pre = pre

    def moveToHead(self, node):
        node.remove()
        self.add(node)

    def popTail(self):
        res = self.pre
        self.remove()
        return res

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.head = DLinkedNode(None, None)
        self.tail = DLinkedNode(None, None)
        self.head.post = self.tail
        self.tail.pre = self.head
        self.dic = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            self.head.moveToHead(self.dic[key])
            return self.dic[key].value
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.dic[key].value = value
            self.dic[key].key = key
            self.head.moveToHead(self.dic[key])
        else:
            newNode = DLinkedNode(key, value)
            self.dic[key] = newNode
            self.head.add(newNode)
            
            self.count += 1
            
            if self.count > self.capacity:
                self.tail = self.tail.popTail()
                del self.dic[self.tail.key]
                self.count -= 1
            
            
        
        
            

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


# Another version from discussion
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
    
    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

# 2017.02.23
# Not O(1) version
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxCapacity = capacity
        self.mp = {}
        self.cache = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mp:
            kv = self.mp[key]
            self.cache.remove(kv)
            self.cache.append(kv)
            return kv[1]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        kv = [key, value]
        if key in self.mp:
            self.mp[key][1] = value
            self.cache.remove(self.mp[key])
            self.cache.append(self.mp[key])
        else:
            if len(self.cache) == self.maxCapacity:
                tmp = self.cache[0]
                del self.cache[0]
                del self.mp[tmp[0]]
            self.cache.append(kv)
            self.mp[key] = kv

