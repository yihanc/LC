# 56. Merge Intervals   QuestionEditorial Solution  My Submissions
# Total Accepted: 91908
# Total Submissions: 331076
# Difficulty: Hard
# Contributors: Admin
# Given a collection of intervals, merge all overlapping intervals.
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
# Subscribe to see which companies asked this question
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        
        for x in sorted(intervals, key=lambda i: i.start):
            if res and res[-1].end >= x.start:
                res[-1].end = max(res[-1].end, x.end)
            else:
                res.append(x)
        
        return res
             
