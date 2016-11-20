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

if __name__ == "__main__":
    ratings = [1,2,1,3,4,10,1,2,3]
    print(ratings)
    print(Solution().candy(ratings))




# Too slow Failed at large case..
# class Solution(object):
#     found = False
#     def candy(self, ratings):
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         res = [ 0 ] * len(ratings)
#         self.dfs(ratings, res, 0)
#         print(res)
#         return sum(res)
#             
#     def dfs(self, ratings, res, i):
#         if self.found:
#             return
# 
#         if i == len(ratings):
#             self.found = True
#             return
#         
#         if i > 0 and ratings[i] > ratings[i-1]:
#             value = res[i-1] + 1
#         else:
#             value = 1
#             
#         while not self.found:
#             print("i: ", i)
#             res[i] = value
#             self.dfs(ratings, res, i+1)
#             if self.found:
#                 return
#             res[i] = 0
#             value += 1
# 
