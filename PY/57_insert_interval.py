# 57. Insert Interval   QuestionEditorial Solution  My Submissions
# Total Accepted: 75076
# Total Submissions: 290951
# Difficulty: Hard
# Contributors: Admin
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their start times.
# 
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# 
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
# 
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# 
# Subscribe to see which companies asked this question
# Definition for an interval.
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 2018.02.23 
# One pass no insert version
# Assuming intervals were sorted
# If not sorted, insert newInterval and then sort is easier
# 69ms

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        inserted = False
        i = 0
        while i < len(intervals) or not inserted:                # Need "or not inserted" to handle finished but newInterval has not been inserted case
            if (i == n) or (not inserted and intervals[i].start > newInterval.start):
                cur, inserted = newInterval, True   # Not changing i
            else:
                cur, i = intervals[i], i + 1
                
            if not res or res[-1].end < cur.start:  # No overlap with res[-1]
                res.append(cur)
            else:                                   # Overlap. Update res[-1] only
                res[-1].end = max(res[-1].end, cur.end)
        return res



# o(n) solution slower
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        n = len(intervals)
        for i in xrange(n):                     # Insert first.
            if newInterval.start < intervals[i].start:
                intervals.insert(i, newInterval)
                break
            
        if n == len(intervals):
            intervals.append(newInterval)
        
        for x in intervals:                     # Then merge using same idea of #56
            if res and x.start <= res[-1].end:
                res[-1].end = max(x.end, res[-1].end)
            else:
                res.append(x)

        return res
