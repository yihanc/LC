# 135. Candy   QuestionEditorial Solution  My Submissions
# Total Accepted: 60931
# Total Submissions: 257062
# Difficulty: Hard
# Contributors: Admin
# There are N children standing in a line. Each child is assigned a rating value.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 

# Algorithms. Left right scan
# 1. Scan left.
# 2. Scan right and update
# 3. Get sum
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """        
        n = len(ratings)
        res = [ 1 for x in xrange(n) ]
        
        for i in xrange(1,n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in xrange(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)

        return sum(res)

if __name__ == "__main__":
    ratings = [1,2,1,3,4,10,1,2,3]
    print(ratings)
    print(Solution().candy(ratings))
