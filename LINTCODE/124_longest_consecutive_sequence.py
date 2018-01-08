

# 12.30.2017

class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        S = set(num)
        res = 1
        for num in S:
            if num - 1 not in S:
                count = 0
                while num in S:
                    num = num + 1
                    count += 1
                res = max(count, res)
        return res
            
