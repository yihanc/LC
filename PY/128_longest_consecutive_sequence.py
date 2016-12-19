# 128. Longest Consecutive Sequence   QuestionEditorial Solution  My Submissions
# Total Accepted: 84089
# Total Submissions: 242038
# Difficulty: Hard
# Contributors: Admin
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.
# 
# Subscribe to see which companies asked this question

# 12.4.2016 Set method.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in nums:
                i = 1
                while num + i in nums:
                    i += 1
                res = max(res, i)
                
        return res
        

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        n = len(nums)
        for i in xrange(n):
            print(" nums[i]: ", nums[i])
            print(dic)
            if nums[i] in dic:
                continue
            else:
                left, right = 0, 0
                if nums[i] - 1 in dic:
                    left = dic[nums[i]-1]
                if nums[i] + 1 in dic:
                    right = dic[nums[i]+1]
                
                boundary = left + right + 1
                res = max(res, boundary)
                print(" res: ", res)
                
                dic[nums[i]] = boundary     # Keep missing this 
                dic[nums[i] - left] = boundary
                dic[nums[i] + right] = boundary
                
        return res


if __name__ == "__main__":
    # nums = [ 100, 4, 200, 1, 3, 2]
    nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    print("res : ", Solution().longestConsecutive(nums))
