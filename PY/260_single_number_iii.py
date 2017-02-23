# 260. Single Number III   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 54369
# Total Submissions: 111552
# Difficulty: Medium
# Contributors: Admin
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# 
# For example:
# 
#     Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# 
#     Note:
#         The order of the result is not important. So in the above example, [5, 3] is also correct.
#         Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#         Credits:
#             Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
#             Subscribe to see which companies asked this question
                    
# Two passes solution. Two group solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        diff = diff & (-diff)   # Get the right most bit
        
        res = [0, 0]
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
        
        

# This is not o(n) space. dic may go up to o(n/2) space.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        
        for num in nums:
            if num in dic:
                del dic[num]
            else:
                dic[num] = True
        
        res = []
        for num in dic:
            res.append(num)

        return res

if __name__ == "__main__":
    Solution().singleNumber([1,2,1,3,2,5])
                    
