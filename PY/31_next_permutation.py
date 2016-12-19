# 31. Next Permutation My Submissions QuestionEditorial Solution
# Total Accepted: 67474 Total Submissions: 252359 Difficulty: Medium
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3  1,3,2
# 3,2,1  1,2,3
# 1,1,5  1,5,1
#
# Analysis:
# 12, 21
# 123, 132, 213, 231, 312, 321
# 1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431
# 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321
#
# 
# 1234, 4>3? y, 1243
# 1243, 3>4? n. 3>2? y yes, sort right 1342, 2<4, 1324
# 1324, 4>2? y 1342
# 1342, 2>4?, no. 2>3? no. 4>3? yes, swap 1432, sort right, 1423
# 1423, s32, 1432
# 1432, 2<3<4, 2143, 2134
# 2134, 4>3, 2143
#
# So we could see the algorithms below:
# i = len() - 2, j from len(nums) -1 to i, check if we could find nums[j] > nums[i] on the right
# if yes, swap nums[i], [j]
# if no, i--
# Sort nums[i+1:] before returning
#
# Subscribe to see which companies asked this question

# 12.17 Rewrite. Better
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i != -1:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        return

# 11.22.2016. This is better
# Use i, j to find the two to swap

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
#        print(nums)
        n = len(nums)
        if n <= 1: return
        
        i = n - 2
        while i >= 0:
            j = n - 1
#            print("i: " + str(i) + " j: " + str(j))
            while j > i and nums[i] >= nums[j]:         #Fail case [151] without "="
                j -= 1

            if j != i: # Found! 
                nums[i], nums[j] = nums[j], nums[i]     #1 Swap nums[i], [j]
                break
            else: 
                i -= 1 

        #2 Sort nums[i+1:]
        i, j = i+1, n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
#        print(nums)
#        print("")
        return nums
            
import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        A = Solution().nextPermutation([1,2])
        B = [2,1]
        self.assertEqual(A, B)

    def test_1(self):
        A = Solution().nextPermutation([2,1])
        B = [1,2]
        self.assertEqual(A, B)

    def test_2(self):
        A = Solution().nextPermutation([1,2,3])
        B = [1,3,2]
        self.assertEqual(A, B)

    def test_3(self):
        A = Solution().nextPermutation([1,2,3,4])
        B = [1,2,4,3]
        self.assertEqual(A, B)

    def test_4(self):
        A = Solution().nextPermutation([1,2,4,3])
        B = [1,3,2,4]
        self.assertEqual(A, B)

    def test_5(self):
        A = Solution().nextPermutation([4,1,2,3])
        B = [4, 1, 3, 2]
        self.assertEqual(A, B)

    def test_6(self):
        A = Solution().nextPermutation([1,3,2,4])
        B = [1,3,4,2]
        self.assertEqual(A, B)

    def test_7(self):
        A = Solution().nextPermutation([1,3,4,2])
        B = [1,4,2,3]
        self.assertEqual(A, B)

    def test_8(self):
        A = Solution().nextPermutation([1,4,2,3])
        B = [1,4,3,2]
        self.assertEqual(A, B)

    def test_9(self):
        A = Solution().nextPermutation([1,4,3,2])
        B = [2,1,3,4]
        self.assertEqual(A, B)

    def test_10(self):
        A = Solution().nextPermutation([1,1,5])
        B = [1,5,1]
        self.assertEqual(A, B)

    def test_11(self):
        A = Solution().nextPermutation([1,5,1])
        B = [5,1,1]
        self.assertEqual(A, B)

    def test_12(self):
        A = Solution().nextPermutation([5, 4,3,2,1])
        B = [1,2,3,4,5]
        self.assertEqual(A, B)

if __name__ == "__main__":
    unittest.main()
