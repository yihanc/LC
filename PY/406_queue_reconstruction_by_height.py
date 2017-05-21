# 406. Queue Reconstruction by Height Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 22110
# Total Submissions: 40292
# Difficulty: Medium
# Contributor: LeetCode
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# Note:
# The number of people is less than 1,100.
# 
# Example
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# 2017.05.20
# Better approach
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        if n <= 1: return people
        people = sorted(people, key = lambda x: (-x[0], x[1]))     # sort desc by h and then asc by k
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

# 2017.05.20
# Sort and then insert one by one
# Self wrote. There is a simpler way
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        if n <= 1: return people
        people = sorted(people, key = lambda x: (-x[0], x[1]))     # sort desc by h and then asc by k
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        print(people)
        res = [people[0]]
        
        for i in xrange(1, n):
            h, k = people[i]
            cnt = 0
            #print(res, h, k)
            for j in xrange(len(res) + 1):
                if cnt == k:
                    res.insert(j, people[i])
                    break
                if res[j][0] >= people[i][0]:
                    cnt += 1
                j += 1
            
        return res
