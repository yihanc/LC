# 162. Find Peak Element  QuestionEditorial Solution  My Submissions
# Total Accepted: 81586
# Total Submissions: 235435
# Difficulty: Medium
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] != num[i+1], find a peak element and return its index.
# 
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -00
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
# 
# click to show spoilers.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            # When to return
            if (( mid - 1 < 0 or nums[mid] > nums[mid -1] ) and
                ( mid + 1 >= len(nums) or nums[mid] > nums[mid + 1] )):
                return mid
            # When to search left
            elif mid - 1 >= 0 and nums[mid] <= nums[mid-1]:
                end = mid - 1
            # When to search right
            else:
                start = mid + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([0]))
    print(sol.findPeakElement([1,2]))
    print(sol.findPeakElement([1,2,3]))
    print(sol.findPeakElement([1,2,3,1]))

# Test Cases
# [0]
# [1,2]
# [1,2,3]
# [1,2,3,1]

