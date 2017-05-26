# 253. Meeting Rooms II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 36968
# Total Submissions: 95507
# Difficulty: Medium
# Contributor: LeetCode
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# 
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Differences between Merge intervals and meeting rooms
# In "MERGE INTERVALS", it merge if it overlap
# In "MEETING ROOM", it merge if they don't intersecs

# 2017.05.26
# Sort interval + heapq sort by end of minimum
# 
from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 0: return len(intervals)
        s_ints = sorted(intervals, key = lambda x: (x.start, -x.end))
        hq = []
        heappush(hq, [s_ints[0].end, s_ints[0].start])
        
        for i in xrange(1, len(s_ints)):
            if hq and s_ints[i].start >= hq[0][0]:
                tmp = heappop(hq)
                tmp[0] = max(tmp[0], s_ints[i].end)
                heappush(hq, tmp)
            else:
                heappush(hq, [s_ints[i].end, s_ints[i].start])

        return len(hq)


