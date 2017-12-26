# 57. 3Sum 
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
#  Notice
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# 
# The solution set must not contain duplicate triplets.
# 
# Have you met this question in a real interview? Yes
# Example
# For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# 
# (-1, 0, 1)
# (-1, -1, 2)

class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3: return []
        numbers.sort()
        #print(numbers)
        res = []
        i = 0
        while i < len(numbers) - 2:
            if i > 0 and numbers[i] == numbers[i-1]:
                i += 1
                continue
            
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    j += 1
                    continue
                if k < len(numbers) - 1 and numbers[k] == numbers[k + 1]:
                    k -= 1
                    continue

                print(i, j, k)
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    #print("ANSWER")
                    res.append([numbers[i], numbers[j], numbers[k]])
                    k -= 1
                    j += 1
                elif numbers[i] + numbers[j] + numbers[k] > 0:
                    k -= 1
                else:
                    j += 1
                
            i += 1
        return res
        
