# 11. Container With Most Water My Submissions QuestionEditorial Solution
# Total Accepted: 79027 Total Submissions: 227020 Difficulty: Medium
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container.
import unittest

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1: return 0

        i, j, area = 0, len(height) - 1, 0
        while i < j:
            print(height[j])
            print(j)
            print(i)
            if height[i] < height[j]:
                area = max(area, height[i] * (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1
        return area

class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().maxArea([1, 1]), 1)

if __name__ == "__main__":
    # Solution().maxArea([1,1])
    unittest.main()
        
