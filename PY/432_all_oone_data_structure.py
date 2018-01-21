# 432. All O`one Data Structure
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Implement a data structure supporting the following operations:
# 
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.


# 2018.01.15
# Similar to LFU except Each Double LinkedList value is a set
# Use DDLinkedList (key is frequency)  + Dictionary + Set

# DD LinkedList (Frequency, set([]) + dictionary

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.head = ddNode(-1)
        self.tail = ddNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        #print("-- Inserting", key)
        if key not in self.dic: # Add to head's next
            if self.head.next.key != 1: # Check to see if need to create a new node
                node = ddNode(1)
                self.ddInsertNode(node, self.head)
            else:
                node = self.head.next
            node.value.add(key)
            self.dic[key] = node            # update dic
        else:   # Remove from current node and add to next node
            cur_node = self.dic[key]
            next_node = cur_node.next
            if cur_node.next.key != cur_node.key + 1:  # add new node
                next_node = ddNode(cur_node.key + 1)
                self.ddInsertNode(next_node, cur_node)
            next_node.value.add(key)
            self.ddRemoveKeyFromNode(cur_node, key)    # Remove from cur_node
            self.dic[key] = next_node           # Update dic last
        #self.printAll()

            
    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        #print("Deleting key", key)
        if key not in self.dic:
            return
        else:
            cur_node = self.dic[key]
            prev_node = cur_node.prev
            if cur_node.key == 1:   # Just delete if == 1
                self.ddRemoveKeyFromNode(cur_node, key)
                del self.dic[key]
            else:   
                if prev_node.key != cur_node.key - 1:       # Need to insert a prev node
                    prev_node = ddNode(cur_node.key - 1)
                    self.ddInsertNode(prev_node, cur_node.prev)
                prev_node.value.add(key)
                self.ddRemoveKeyFromNode(cur_node, key)
                self.dic[key] = prev_node

                
    def printAll(self):         # Func to help debug
        print("Printing from start")
        cur = self.head
        while cur:
            print(cur.key, cur.value)
            cur = cur.next
        #print("Printing dic", self.dic)

        
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        ddNodeMax = self.tail.prev
        if ddNodeMax == self.head: return ""
        for ele in ddNodeMax.value:
            return ele

        
    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        ddNodeMin = self.head.next
        if ddNodeMin == self.tail: return ""
        for ele in ddNodeMin.value:
            return ele
    
    
    def ddInsertNode(self, node, pos_node):
        n1, n2 = pos_node, pos_node.next
        n1.next, n2.prev = node, node
        node.prev, node.next = n1, n2


    def ddRemoveNode(self, node):
        n1, n2 = node.prev, node.next
        n1.next, n2.prev = n2, n1
        node.prev, node.next = None, None

        
    def ddRemoveKeyFromNode(self, node, key):   # also cleans up node if nothing in the node
        node.value.remove(key)
        if len(node.value) == 0:
            self.ddRemoveNode(node)

    
class ddNode(object):   # Double Linked List node, Key is frequency
    def __init__(self, k):
        self.key = k
        self.value = set([])
        self.prev = None
        self.next = None
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
