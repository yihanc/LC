# 60. Search Insert Position 
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume NO duplicates in the array.
# 
# Have you met this question in a real interview? Yes
# Example
# [1,3,5,6], 5 → 2
# 
# [1,3,5,6], 2 → 1
# 
# [1,3,5,6], 7 → 4
# 
# [1,3,5,6], 0 → 0


LntCode
Problem
Ladder
Contest
Favorites
Submissions
Group
Help

Search for problems or tags
Language 
Sherry Di Shao 
60. Search Insert Position 
 Description
 Notes
 Testcase
 Judge
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

Challenge 
Tags 
 
60. Search Insert Position 
 Description
 Notes
 Testcase
 Judge
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 060. Search Insert Position 
 Description
 Notes
 Testcase
 Judge
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A or len(A) == 0: return 0
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] == target or (target < A[mid] and (mid == 0 or target > A[mid-1])) :
                return mid
            elif target > A[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l if target <= A[l]  else l + 1
            
