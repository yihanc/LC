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

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return
    
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:  # Find i
            i -= 1

        print("i", i)
        
        if i == -1:  # Case 4 3 2 1
            j, k = 0, n - 1
            while j < k:
                nums[j], nums[k] = nums[k], nums[j]
                j, k = j + 1, k - 1
            return
        
        just_bigger = i + 1              # Found i is the one bigger. #  132883727654321, 3 7654221
        j = i + 1
        while j < n:
            if nums[i] < nums[j] and nums[j] < nums[just_bigger] :
                just_bigger = j
            j += 1
        print("just_bigger", just_bigger)
            
        nums[i], nums[just_bigger] = nums[just_bigger], nums[i] # Swap
        while just_bigger + 1 < n and nums[just_bigger] < nums[just_bigger + 1]:
            nums[just_bigger], nums[just_bigger+1] = nums[just_bigger+1], nums[just_bigger]
            just_bigger += 1
        print(nums)
        
        j, k = i + 1, n - 1             # Reverse sort j +1 to end
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j, k = j + 1, k - 1
        
        return


if __name__ == "__main__":
#    nums = [1,3,2]
    nums = [2,3,1,3,3]
    print("start", nums)
    Solution().nextPermutation(nums)
    print("end", nums)
