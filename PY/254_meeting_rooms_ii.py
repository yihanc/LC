# [20] 253    Meeting Rooms II
# 
# 35.0%   Medium
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],] (si < ei), find the minimum number of conference rooms required.
# 
# For example,
# Given [[0, 30],[5, 10],[15, 20]], return 2.

from heapq import *
def meeting(intervals):
    if not intervals: return 0
    hq = []
    heappush(hq
    
    return


if __name__ == "__main__":
    nums = [[0, 30], [5, 10], [15,20]]
    if assert meeting(nums) == 2:
        print("correct")
