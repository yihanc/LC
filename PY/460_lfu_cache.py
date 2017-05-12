# 460. LFU Cache Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 9534 Total Submissions: 42295 Difficulty: Hard
# Contributors: 1337c0d3r  , fishercoder
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# Subscribe to see which companies asked this question.

# 2017.05.09 Double Linked List + 2 Dict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.keymap = {}
        self.fremap = {}
        self.minfre = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keymap:
            return -1
        else:
            node = self.keymap[key]
            node.fre += 1
            self.ddRemove(node)
            if self.fremap[self.minfre].next is self.fremap[self.minfre]:
                self.minfre += 1
            root = self.fremap.setdefault(node.fre, DoubleListNode(None, None))
            self.ddAddToTail(node, root)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0: return
        if key in self.keymap:
            self.keymap[key].value = value
            self.get(key)
        else:
            if len(self.keymap) == self.cap:
                root = self.fremap[self.minfre]
                keytbd = root.next.key
                self.ddRemove(root.next)
                del self.keymap[keytbd]
            node, self.minfre = DoubleListNode(key, value), 1
            root = self.fremap.setdefault(self.minfre, DoubleListNode(None, None))
            self.ddAddToTail(node, root)
            self.keymap[key] = node

                
    def ddRemove(self, node):
        n1, n2 = node.prev, node.next
        n1.next, n2.prev = n2, n1
        node.prev, node.next = None, None

        
    def ddAddToTail(self, node, tail):
        n1, n2 = tail.prev, tail
        node.prev, node.next = n1, n2
        n1.next, n2.prev = node, node

class DoubleListNode(object):
    def __init__(self, key, value):
        self.fre = 1
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


# 2017.05.08 Best online version
# val_node = [ PREV, NEXT, KEY, VALUE, FRE ] double linked list
# key_map dic{ key: val_node }  to fast query
# freq_map: dic{ fre: val_node } for 
PREV,NEXT,KEY,VAL,FREQ = 0,1,2,3,4
class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.freq_map = {}
        self.key_map = {}
        self.min_freq = 1

    def get(self, key):
        key_map, freq_map = self.key_map, self.freq_map
        if key not in key_map:
            return -1
        else:
            val_node = key_map[key]
            val_node[PREV][NEXT],val_node[NEXT][PREV] = val_node[NEXT],val_node[PREV]
            if freq_map[self.min_freq] is freq_map[self.min_freq][NEXT]:    #EMPTY list
                self.min_freq+=1
            freq = val_node[FREQ]
            root = freq_map.setdefault(freq+1,[])
            if not root:
                root[:] = [root,root,None,None,freq+1]
            val_node[PREV],val_node[NEXT] = root[PREV],root
            val_node[FREQ]+=1
            root[PREV][NEXT] = root[PREV] = val_node
            return key_map[key][VAL]

    def put(self, key, value):
        key_map, freq_map, cap = self.key_map, self.freq_map, self.capacity
        if not cap:
            return
        if key in key_map:
            key_map[key][VAL] = value
            self.get(key)
        else:
            if len(key_map) == cap:
                root = freq_map[self.min_freq]
                node_evict = root[NEXT]
                root[NEXT],node_evict[NEXT][PREV] = node_evict[NEXT], root
                del key_map[node_evict[KEY]]
            self.min_freq = 1
            val_node = [None,None,key,value,1]
            root = freq_map.setdefault(1,[])
            if not root:
                root[:] = [root,root,None,None,1]
            val_node[PREV],val_node[NEXT] = root[PREV],root
            root[PREV][NEXT] = root[PREV] = val_node
            key_map[key] = val_node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 2017.05.08 Use deque and frelist. 
# Might need to change to DoubleLinkedList to achieve O(1)
# Idea explained
# use dic to keep track of node location { key: node }
# use list + deque to save element (Ideally this should be double linked list to optimize)
# when get(), check dic for fast retrivel
# when put(), update list deque

from collections import deque
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dic = {}
        self.frelist = []
        self.frelistlen = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.frelist[node.fre].remove(node)
            node.fre += 1
            while len(self.frelist) <= node.fre:
                self.frelist.append(deque())
            self.frelist[node.fre].append(node)
            return node.v
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0: return
        if key not in self.dic:
            if self.frelistlen == self.cap:
                for x in self.frelist:
                    if len(x) > 0:
                        keytbd = x[0].k
                        x.popleft()
                        self.frelistlen -= 1
                        del self.dic[keytbd]
                        break
            node = LFUNode(key, value)
            while len(self.frelist) <= node.fre:    # initialize frelist element
                self.frelist.append(deque())
            self.frelist[node.fre].append(node)
            self.frelistlen += 1
            self.dic[key] = node
        else:
            node = self.dic[key]
            self.frelist[node.fre].remove(node)
            node.fre, node.v = node.fre + 1, value
            while len(self.frelist) <= node.fre:
                self.frelist.append(deque())
            self.frelist[node.fre].append(node)

        
class LFUNode(object):
    def __init__(self, k, v):
        self.fre = 0
        self.k = k
        self.v = v

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
