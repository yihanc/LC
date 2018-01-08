

# 12.31.2017
# Another way

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not newInterval and not intervals: return []
        res = []
        i = 0
        while i <= len(intervals):
            if i == len(intervals) or newInterval.start <= intervals[i].start:
                the_rest = [newInterval] + intervals[i:]
                newInterval = None
                break
            
            res.append(intervals[i])
            i += 1
            
        #print(res)
        
        for i in xrange(len(the_rest)):
            if res and res[-1].end >= the_rest[i].start:
                res[-1].end = max(res[-1].end, the_rest[i].end)
            else:
                res.append(the_rest[i])
        return res

