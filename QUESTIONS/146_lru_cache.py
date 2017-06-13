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

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

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
