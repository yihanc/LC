# 33. Search in Rotated Sorted Array My Submissions QuestionEditorial Solution
# Total Accepted: 104226 Total Submissions: 341737 Difficulty: Hard
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([0], 0))
    print(sol.search([0], 1))
    print(sol.search([0,1], 0))
    print(sol.search([0,1], 1))
    print(sol.search([0,1], 2))
    print(sol.search([1,0], 0))
    print(sol.search([1,0], 1))
    print(sol.search([1,0], 2))
    print(sol.search([2,3,1], 2))
    print(sol.search([2,3,1], 3))
    print(sol.search([2,3,1], 1))
    print(sol.search([2,3,1], 4))
    print(sol.search([3,1,2], 3))
    print(sol.search([3,1,2], 1))
    print(sol.search([3,1,2], 2))
    print(sol.search([3,1,2], 4))
    print(sol.search([1,2,3], 1))
    print(sol.search([1,2,3], 2))
    print(sol.search([1,2,3], 3))
    print(sol.search([1,2,3], 4))

# Test cases
# [0] 1
# [0 1] -1
# [0 1] 1
# [1 0] 2
# [1 0] 0
# [1 0] 1
# [2, 3, 1] 2
# [3, 1, 2] 3
# [1, 2, 3] 1
# 0 1 2 3 4 5 6 7
# 6 7 0 1 2 3 4
# 7 0 2 4 5 6 
# 5 6 7 8 0 1 2
