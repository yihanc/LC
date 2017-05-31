# 362. Design Hit Counter Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14528
# Total Submissions: 27191
# Difficulty: Medium
# Contributor: LeetCode
# Design a hit counter which counts the number of hits received in the past 5 minutes.
# 
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
# 
# It is possible that several hits arrive roughly at the same time.
# 
# Example:
# HitCounter counter = new HitCounter();
# 
# // hit at timestamp 1.
# counter.hit(1);
# 
# // hit at timestamp 2.
# counter.hit(2);
# 
# // hit at timestamp 3.
# counter.hit(3);
# 
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
# 
# // hit at timestamp 300.
# counter.hit(300);
# 
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
# 
# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?


# 2017.05.27
# times and hits bucket
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [ 0 for x in xrange(300) ]
        self.hits = [ 0 for x in xrange(300) ]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for i in xrange(300):
            if timestamp - self.times[i] < 300:
                count += self.hits[i]
        return count
        
