# 42. Trapping Rain Water My Submissions QuestionEditorial Solution
# Total Accepted: 68613 Total Submissions: 210598 Difficulty: Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

if __name__ == "__main__":
#    height = [5,4,1,2]
#    print(Solution().trap(b))
    height = [5,2,1,2,1,5]      # Top [5, 2, 5]
#    height = [5,5,1,7,1,1,5,2,7,6]
#    height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
#    height = [8,8,1,5,6,2,5,3,3,9]

    print(Solution().trap(height))
