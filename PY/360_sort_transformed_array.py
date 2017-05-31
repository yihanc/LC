# 360. Sort Transformed Array Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 10435
# Total Submissions: 23870
# Difficulty: Medium
# Contributor: LeetCode
# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
# 
# Result: [3, 9, 15, 33]
# 
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
# 
# Result: [-23, -5, 1, 7]
# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.


import bisect
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def getres(num):
            return a*(num**2) + (b*num) + c
        print(nums)    
        l, r = 0, len(nums) - 1
        isUp = True if a > 0 else False     # Open up or down if open up. l and r and the highest. if open down. l and r could be the lowest
        res = []
        while l < r:
            ll, rr = getres(nums[l]), getres(nums[r])
            #print(ll, rr)
            if isUp and ll > rr or not isUp and ll < rr:
                res.append(ll)
                l += 1
            else:
                res.append(rr)
                r -= 1
        res.append(getres(nums[l]))
        return res[::-1] if isUp else res


if __name__  == "__main__":
    nums = [-100, -100, -89, -85, -82, -79, -75, -72, -69, -64, -62, -53, -41, -41, -40, -34, -28, -26, -26, -26, -25, -24, -19, -18, -11, -3, 8, 8, 12, 17, 19, 19, 29, 30, 32, 48, 48, 50, 67, 67, 78, 88, 89, 98]
    a, b, c = -96, -49, -35
    # for num in nums:
#         print(a*(num**2) + b*num + c, num)
    print(Solution().sortTransformedArray(nums, a, b, c))


# cases
# [-100, -100, -89, -85, -82, -79, -75, -72, -69, -64, -62, -53, -41, -41, -40, -34, -28, -26, -26, -26, -25, -24, -19, -18, -11, -3, 8, 8, 12, 17, 19, 19, 29, 30, 32, 48, 48, 50, 67, 67, 78, 88, 89, 98]
