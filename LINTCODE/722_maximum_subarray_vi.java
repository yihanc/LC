import java.lang.*;

public class Solution {
    /*
     * @param : the array
     * @return: the max xor sum of the subarray in a given array
     */
    public int maxXorSubarray(int[] nums) {
        // write code here
        int pre = 0;
        Trie trie = new Trie();
        int res = Integer.MIN_VALUE;
        
        for (int i = 0; i < nums.length; i++) {
            pre = pre ^ nums[i];
            trie.insert(pre);
            res = Math.max(res, trie.query(pre));
        }
        return res;
    }
}

class Trie {
    private TrieNode root;
    private int INTBITS = 32;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(int x) {
        TrieNode p = root;
        for (int i = INTBITS - 1; i >= 0; i-- ) {
            int v = ((x & (1 << i)) > 0) ? 1 : 0;
            v = v > 0 ? 1 : 0;
            if (p.next[v] == null)
                p.next[v] = new TrieNode();
            p = p.next[v];
        }
        p.val = x;
    }
    
    public int query(int x) {
        TrieNode p = root;
        System.out.println("x:  " + x);

        for (int i = INTBITS - 1; i >= 0; i-- ) {
            int v = ((x & (1 << i)) > 0) ? 1 : 0;
            if (p.next[1-v] != null) {
                p = p.next[1-v];
            } else if (p.next[v] != null) {
                p = p.next[v];
            }
        }
        return x ^ p.val;
    }
}

class TrieNode {
    TrieNode[] next = new TrieNode[2];
    int val = 0;
}
