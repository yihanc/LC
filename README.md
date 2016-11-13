# LC

## Category

### Tree and Divide & Conquer
### inorder (recur, iter + stack, morris)
### preorder (recur, iter + stack, morris)
### postorder (recur, iter + stack, iter + 2 stack, morris?)

94  Binary Tree Inorder Traversal   41.9%   Medium
95  Unique Binary Search Trees II   29.9%   Medium
96  Unique Binary Search Trees  38.9%   Medium
98  Validate Binary Search Tree 21.7%   Medium
99  Recover Binary Search Tree  27.9%   Hard
100 Same Tree   44.4%   Easy
101 Symmetric Tree  35.7%   Easy
102 Binary Tree Level Order Traversal   35.1%   Easy
103 Binary Tree Zigzag Level Order Traversal    30.6%   Medium
104 Maximum Depth of Binary Tree    49.6%   Easy
105 Construct Binary Tree from Preorder and Inorder Traversal   29.9%   Medium
106 Construct Binary Tree from Inorder and Postorder Traversal  30.2%   Medium
107 Binary Tree Level Order Traversal II    36.2%   Easy
108 Convert Sorted Array to Binary Search Tree  39.2%   Medium
110 Balanced Binary Tree    35.4%   Easy
111 Minimum Depth of Binary Tree    31.6%   Easy
112 Path Sum    32.2%   Easy
113 Path Sum II 30.0%   Medium
114 Flatten Binary Tree to Linked List  32.5%   Medium
116 Populating Next Right Pointers in Each Node 36.7%   Medium
117 Populating Next Right Pointers in Each Node II  33.1%   Hard
124 Binary Tree Maximum Path Sum    24.3%   Hard
129 Sum Root to Leaf Numbers    34.2%   Medium
144 Binary Tree Preorder Traversal  41.7%   Medium
145 Binary Tree Postorder Traversal 37.1%   Hard
156 Binary Tree Upside Down     40.4%   Medium
173 Binary Search Tree Iterator 37.0%   Medium
199 Binary Tree Right Side View 37.1%   Medium
222 Count Complete Tree Nodes   26.4%   Medium
226 Invert Binary Tree  48.2%   Easy
230 Kth Smallest Element in a BST   40.4%   Medium
235 Lowest Common Ancestor of a Binary Search Tree  37.7%   Easy
236 Lowest Common Ancestor of a Binary Tree 29.1%   Medium
250 Count Univalue Subtrees     38.9%   Medium
255 Verify Preorder Sequence in Binary Search Tree  37.8%   Medium
257 Binary Tree Paths   32.1%   Easy
270 Closest Binary Search Tree Value    36.2%   Easy
272 Closest Binary Search Tree Value II     35.7%   Hard
285 Inorder Successor in BST    36.4%   Medium
297 Serialize and Deserialize Binary Tree   29.9%   Hard
298 Binary Tree Longest Consecutive Sequence    38.5%   Medium
333 Largest BST Subtree     28.4%   Medium
337 House Robber III    40.0%   Medium
366 Find Leaves of Binary Tree  54.8%   Medium


### Binary Search
4   Median of Two Sorted Arrays 19.9%   Hard
29  Divide Two Integers     15.9%   Medium
33  Search in Rotated Sorted Array  31.3%   Hard
34  Search for a Range  30.2%   Medium
35  Search Insert Position  38.4%   Medium
50  Pow(x, n)   27.4%   Medium
69  Sqrt(x) 26.3%   Medium
74  Search a 2D Matrix  35.1%   Medium
81  Search in Rotated Sorted Array II   32.6%   Medium
153 Find Minimum in Rotated Sorted Array    37.7%   Medium
154 Find Minimum in Rotated Sorted Array II 35.5%   Hard
162 Find Peak Element   34.7%   Medium
167 Two Sum II - Input array is sorted  48.5%   Medium
174 Dungeon Game    22.2%   Hard
209 Minimum Size Subarray Sum   27.9%   Medium
222 Count Complete Tree Nodes   26.4%   Medium
230 Kth Smallest Element in a BST   40.5%   Medium
240 Search a 2D Matrix II   36.6%   Medium
270 Closest Binary Search Tree Value    36.3%   Easy
275 H-Index II  33.1%   Medium
278 First Bad Version   23.7%   Easy
287 Find the Duplicate Number   40.7%   Hard
300 Longest Increasing Subsequence  36.3%   Medium
302 Smallest Rectangle Enclosing Black Pixels   41.5%   Hard
349 Intersection of Two Arrays  44.5%   Easy
350 Intersection of Two Arrays II   42.5%   Easy
354 Russian Doll Envelopes  30.6%   Hard
363 Max Sum of Rectangle No Larger Than K   30.4%   Hard
367 Valid Perfect Square    36.8%   Medium
374 Guess Number Higher or Lower    32.1%   Easy
378 Kth Smallest Element in a Sorted Matrix 41.9%   Medium
392 Is Subsequence  44.4%   Medium

binary search
first position of target
last position of target
search insert position
search in a big sorted array
find minimum in rotated sorted array
first bad version
wood cut
count of smaller number
recover rotated sorted array
rotate string

### DFS
* Key points
* nums should be sorted in most cases
* When to append to res? (sum to a value or number of lines or something else?)
* Contain duplicates?
* What to pass to the next level? nums[i:] or nums[i+1:] or nums[:i] + nums[i+1:]

39 combination sum (sorted; Pass nums[i:]; Append line when sum == target)
40 combination sum ii (similar to combination sum ii; Pass nums[i+1]; Append when sum == target; if nums[i] == nums[i-1] continue)
46 permutation  (if not nums append; nums[:i] + nums[i+1:]
47 permutations ii  (similar to permutation; if nums[i] == nums[i-1] continue)
77 combinations (append res.size == n; Pass nums[i+1:])
78 subsets  (sorted; nums[i+1:])
90 subsets ii   (subsets; if nums[i] == nums[i-1] continue)
216 combination sum iii (similar to combination sum ii; Pass nums[i+1]; Append when sum == target; if nums[i] == nums[i-1] continue)

# DP
10  Regular Expression Matching 22.9%   Hard
32  Longest Valid Parentheses   22.8%   Hard
44  Wildcard Matching   18.3%   Hard
53  Maximum Subarray    37.7%   Medium
62  Unique Paths    38.0%   Medium
63  Unique Paths II 30.3%   Medium
64  Minimum Path Sum    36.4%   Medium
70  Climbing Stairs 37.9%   Easy
72  Edit Distance   29.8%   Hard
85  Maximal Rectangle   24.8%   Hard
87  Scramble String 27.6%   Hard
91  Decode Ways 18.2%   Medium
95  Unique Binary Search Trees II   29.9%   Medium
96  Unique Binary Search Trees  38.9%   Medium
97  Interleaving String 23.4%   Hard
115 Distinct Subsequences   30.0%   Hard
118 Pascals triangle
120 Triangle    31.6%   Medium
121 Best Time to Buy and Sell Stock 37.7%   Easy
123 Best Time to Buy and Sell Stock III 27.5%   Hard
132 Palindrome Partitioning II  22.8%   Hard
140 Word Break II   21.1%   Hard
152 Maximum Product Subarray    23.5%   Medium
174 Dungeon Game    22.2%   Hard
188 Best Time to Buy and Sell Stock IV  23.3%   Hard
198 House Robber    36.3%   Easy
213 House Robber II 32.3%   Medium
221 Maximal Square  25.6%   Medium
256 Paint House     44.6%   Medium
264 Ugly Number II  30.5%   Medium
265 Paint House II  36.5%   Hard
276 Paint Fence     32.7%   Easy
279 Perfect Squares 34.3%   Medium
300 Longest Increasing Subsequence  36.3%   Medium
303 Range Sum Query - Immutable 25.9%   Easy
304 Range Sum Query 2D - Immutable  22.6%   Medium
309 Best Time to Buy and Sell Stock with Cooldown   38.7%   Medium
312 Burst Balloons  40.3%   Hard
321 Create Maximum Number   22.7%   Hard
322 Coin Change 25.8%   Medium
338 Counting Bits   58.4%   Medium
343 Integer Break   43.7%   Medium
351 Android Unlock Patterns     39.2%   Medium
354 Russian Doll Envelopes  30.5%   Hard
357 Count Numbers with Unique Digits    44.1%   Medium
361 Bomb Enemy  36.8%   Medium
363 Max Sum of Rectangle No Larger Than K   30.3%   Hard
368 Largest Divisible Subset    31.8%   Medium
375 Guess Number Higher or Lower II 32.1%   Medium
376 Wiggle Subsequence  34.3%   Medium
377 Combination Sum IV  39.9%   Medium
392 Is Subsequence  44.0%   Medium
403 Frog Jump   40.1%   Hard

# Greedy
44  Wildcard Matching   18.4%   Hard
45  Jump Game II    25.8%   Hard
55  Jump Game   29.0%   Medium
122 Best Time to Buy and Sell Stock II  44.3%   Medium
134 Gas Station 28.1%   Medium
135 Candy   23.4%   Hard
253 Meeting Rooms II    36.8%   Medium
316 Remove Duplicate Letters    27.5%   Hard
321 Create Maximum Number   22.9%   Hard
330 Patching Array  30.7%   Hard
358 Rearrange String k Distance Apart   30.2%   Hard
376 Wiggle Subsequence  34.5%   Medium
392 Is Subsequence  44.2%   Medium
402 Remove K Digits 27.5%   Medium

# Linked List
2   Add Two Numbers 24.9%   Medium
19  Remove Nth Node From End of List    31.1%   Easy
21  Merge Two Sorted Lists  36.9%   Easy
23  Merge k Sorted Lists    24.8%   Hard
24  Swap Nodes in Pairs 36.5%   Easy
25  Reverse Nodes in k-Group    28.8%   Hard
61  Rotate List 23.6%   Medium
82  Remove Duplicates from Sorted List II   28.0%   Medium
83  Remove Duplicates from Sorted List  38.0%   Easy
86  Partition List  30.8%   Medium
92  Reverse Linked List II  29.1%   Medium
109 Convert Sorted List to Binary Search Tree   31.8%   Medium
138 Copy List with Random Pointer   26.2%   Hard
141 Linked List Cycle   36.3%   Easy
142 Linked List Cycle II    31.3%   Medium
143 Reorder List    23.9%   Medium
147 Insertion Sort List 30.8%   Medium
148 Sort List   26.3%   Medium
160 Intersection of Two Linked Lists    30.8%   Easy
203 Remove Linked List Elements 30.2%   Easy
206 Reverse Linked List 41.8%   Easy
234 Palindrome Linked List  30.4%   Easy
237 Delete Node in a Linked List    44.7%   Easy
328 Odd Even Linked List    40.6%   Medium
369 Plus One Linked List    51.5%   Medium
379 Design Phone Directory  26.4%   Medium

# String
3   Longest Substring Without Repeating Characters  23.5%   Medium
5   Longest Palindromic Substring   24.0%   Medium
6   ZigZag Conversion   25.6%   Easy
8   String to Integer (atoi)    13.8%   Easy
10  Regular Expression Matching 23.3%   Hard
12  Integer to Roman    42.2%   Medium
13  Roman to Integer    42.8%   Easy
14  Longest Common Prefix   30.2%   Easy
17  Letter Combinations of a Phone Number   31.7%   Medium
20  Valid Parentheses   31.5%   Easy
22  Generate Parentheses    40.9%   Medium
28  Implement strStr()  26.5%   Easy
30  Substring with Concatenation of All Words   21.6%   Hard
32  Longest Valid Parentheses   23.0%   Hard
38  Count and Say   31.9%   Easy
43  Multiply Strings    25.5%   Medium
44  Wildcard Matching   18.7%   Hard
49  Group Anagrams  31.0%   Medium
58  Length of Last Word 30.8%   Easy
65  Valid Number    12.5%   Hard
67  Add Binary  29.9%   Easy
68  Text Justification  17.6%   Hard
71  Simplify Path   23.6%   Medium
72  Edit Distance   30.2%   Hard
76  Minimum Window Substring    23.2%   Hard
87  Scramble String 28.0%   Hard
91  Decode Ways 18.6%   Medium
93  Restore IP Addresses    25.4%   Medium
97  Interleaving String 23.7%   Hard
115 Distinct Subsequences   30.3%   Hard
125 Valid Palindrome    25.0%   Easy
126 Word Ladder II  13.6%   Hard
151 Reverse Words in a String   15.7%   Medium
157 Read N Characters Given Read4   29.4%   Easy
158 Read N Characters Given Read4 II - Call multiple times  24.3%   Hard
159 Longest Substring with At Most Two Distinct Characters  38.7%   Hard
161 One Edit Distance   30.0%   Medium
165 Compare Version Numbers 18.9%   Easy
186 Reverse Words in a String II    28.6%   Medium
214 Shortest Palindrome 22.3%   Hard
227 Basic Calculator II 27.6%   Medium
249 Group Shifted Strings   37.1%   Easy
271 Encode and Decode Strings   26.4%   Medium
273 Integer to English Words    20.7%   Hard
293 Flip Game   53.1%   Easy
336 Palindrome Pairs    23.7%   Hard
340 Longest Substring with At Most K Distinct Characters    38.6%   Hard
344 Reverse String  57.4%   Easy
345 Reverse Vowels of a String  36.8%   Easy
383 Ransom Note 45.5%   Easy
385 Mini Parser 29.1%   Medium
408 Valid Word Abbreviation     26.6%   Easy

