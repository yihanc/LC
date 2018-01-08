
# 1.1.2018
# Double Linked List + Map
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.dict = {}
        self.head = DoubleListNode(-1, -1)
        self.tail = DoubleListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.MAXCAP = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.dict:
            return -1
        else:
            node = self.dict[key]
            self.ddRemove(node)
            self.ddInsertHead(node)
            return node.value


    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.ddRemove(node)
            self.ddInsertHead(node)
        else:
            node = DoubleListNode(key, value)
            if len(self.dict) == self.MAXCAP:
                node_to_remove = self.tail.prev
                self.ddRemove(node_to_remove)
                del self.dict[node_to_remove.key]
            self.ddInsertHead(node)
            self.dict[key] = node
    
    
    def ddInsertHead(self, node):
        n1, n2 = self.head, self.head.next
        n1.next, n2.prev = node, node
        node.prev, node.next = n1, n2
    
    
    def ddRemove(self, node):
        n1, n2 = node.prev, node.next
        node.prev, node.next = None, None
        n1.next, n2.prev = n2, n1
            


class DoubleListNode():
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None
