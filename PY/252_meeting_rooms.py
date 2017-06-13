# 252. Meeting Rooms
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 29727
# Total Submissions: 63708
# Difficulty: Easy
# Contributor: LeetCode
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1: return True
        s_intervals = sorted(intervals, key=lambda x: x.start)
        res = [s_intervals[0]]
        
        for i in xrange(1, len(s_intervals)):
            if s_intervals[i].start < res[-1].end: return False
            res.append(s_intervals[i])
        return True
        
