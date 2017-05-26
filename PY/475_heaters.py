# 475. Heaters Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14490
# Total Submissions: 49183
# Difficulty: Easy
# Contributors:
# neelamgehlot
# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.
# 
# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.


# 2017.05.26
# Algorithm
# Sort heaters
# for house find out where it is suppose to insert
# get min distance from left heater and right heater
# update MAX for each house
from bisect import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters)
        res = 0
        for house in houses:
            i = bisect(heaters, house)      # This finds the index of a sorted array much faster
            if i == len(heaters):
                mindis = house - heaters[i-1]
            elif i == 0:
                mindis = heaters[i] - house
            else:
                mindis = min(house - heaters[i-1], heaters[i] - house) 
            res = max(res, mindis)
        return res
        

# 2017.05.26
# TLS for this case
# ([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923], 
#  [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612])
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        print(houses, heaters)
        if not heaters: return -1
        set_houses = set(houses)

        radius = 0
        while radius < 10 ** 9:
            for pos in heaters:
                if pos + radius in set_houses: set_houses.remove(pos + radius)
                if pos - radius in set_houses: set_houses.remove(pos - radius)
            if len(set_houses) == 0: return radius
            radius += 1
        

