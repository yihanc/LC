# 514. Freedom Trail
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.
# 
# Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.
# 
# Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button. 
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
# If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
# Example:
# 
# 
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
#  For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
#  For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
#  Also, we need 1 more step for spelling.
#  So the final output is 4.
# Note:
# Length of both ring and key will be in range 1 to 100.
# There are only lowercase letters in both strings and might be some duplcate characters in both strings.
# It's guaranteed that string key could always be spelled by rotating the string ring.
# 


# 2018.01.16
# First DP question solved by myself.
# Analysis
# After some observationl, we can see that this question falls under Category 1, Sequential Recurrence Relation 
# From @fun4LeetCode's post at below
# https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs

# So the formula is T(i) = T(i-1) + C

# which means to calculate the minimum steps for i-th char, we need to calculate the state for (i-1)-th char
# And C is: the minimum steps required to move from last_char to char_i
# It is obvious that C is determined by the index of key[i-1] and index of key[i]

# So not only we need to record what is the current char that we are processing,
# We also need another dimension j to save which end position the minimum steps are for.
# Hence, we have DP[i][j] that,  
# where i denotes the i-th char in key, 
# and j denotes the the ending position of char[i],
# and DP[i][j] saves the minimum steps to reach this state

# And also we can determine the state transmation fomular as:
# DP[i][j] = min(DP[i][j], DP[i-1][start] + min(STEPS_LEFT, STEPS_RIGHT) + 1)
# where STEPS_LEFT and STEPS_RIGHT are the minimum steps clockwise/counter-clockwise from index start to index j 

# Time Complexity is O(m*n)

from collections import defaultdict
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(key), len(ring)
        dp = [ [ float('inf') for j in xrange(n)] for i in xrange(m)]
        
        dic = defaultdict(list)
        for i, char in enumerate(ring):
            dic[char].append(i)
        
        for i in xrange(m):
            char = key[i]
            for j in dic[char]:
                if i == 0:
                    dp[i][j] = min(j - 0, n - j) + 1    # For start
                else:
                    last_char = key[i-1]
                    for start in dic[last_char]:
                        left = j - start if j >= start else j - start + n   # Steps if counter-clockwise
                        right = start - j if start >= j else start - j + n   # Steps if clocewise
                        dp[i][j] = min(dp[i][j], dp[i-1][start] + min(left, right) + 1)       
        return min(dp[m-1])
