# 681. Next Closest Time
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
# Example 1:

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        S = set([])
        for char in time:
            S.add(char)
        
        while True:
            time = self.getNextMinute(time)
            if self.checkTime(time, S):
                return time
    
    def checkTime(self, time, S):
        for char in time:
            if char not in S and char != ":":
                return False
        return True
    
    def getNextMinute(self, time):
        hh, mm = time.split(":")
        if hh == "23" and mm == "59":
            return "00:00"
        elif mm == "59":
            return str(int(hh) + 1) + ":00" if int(hh) + 1 >= 10 else "0" + str(int(hh) + 1) + ":00"
        else:
            return hh + ":" + str(int(mm) + 1) if int(mm) + 1 >= 10 else hh + ":0" + str(int(mm) + 1)
        
