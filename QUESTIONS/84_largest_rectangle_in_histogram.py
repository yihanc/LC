# 84. Largest Rectangle in Histogram  QuestionEditorial Solution  My Submissions
# Total Accepted: 71583
# Total Submissions: 284209
# Difficulty: Hard
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# 
# 
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# 
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 
# Subscribe to see which companies asked this question

from collections import deque
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
