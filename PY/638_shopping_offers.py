# 638. Shopping Offers
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# In LeetCode Store, there are some kinds of items to sell. Each item has a price.
# 
# However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
# 
# You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.
# 
# Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.
# 
# You could use any of special offers as many times as you want.
# 
# Example 1:
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation: 
# There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B. 
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
# Example 2:
# Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
# Output: 11
# Explanation: 
# The price of A is $2, and $3 for B, $4 for C. 
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
# You cannot add more items, though only $9 for 2A ,2B and 1C.
# Note:
# There are at most 6 kinds of items, 100 special offers.
# For each item, you need to buy at most 6 of them.
# You are not allowed to buy more items than you want, even if that would lower the overall price.



# 2018.01.21
# DFS + mem
# Mistake: Don't treat price as a special coupon, too slow

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        res = [float('inf')]
        n = len(price)
        reskey = tuple(0 for i in xrange(len(needs)))       # Tuple is hashable in dic
        cache = {reskey: float('inf')}
        self.dfs(price, special, tuple(needs), 0, cache)  
        return cache[reskey]
    
    def dfs(self, price, special, needs, amt, cache):
        if needs in cache and amt >= cache[needs]: return
        cache[needs] = amt
        
        if all([item_need == 0 for item_need in needs]):    #All empty
            return
        
        for coupon in special:
            new_needs = tuple( i - j for i, j in zip(needs, coupon[:-1]) )    # Calculate remaing needs
            if any([item_need < 0 for item_need in new_needs]):     # If any items less than 0, skip
                continue
            if new_needs in cache and amt + coupon[-1] >= cache[new_needs]:   # If already visited and amt is bigger, skip
                continue
            self.dfs(price, special, new_needs, amt + coupon[-1], cache)
            
        # No coupon case
        key = tuple(0 for i in xrange(len(needs)))
        for i,item_need in enumerate(needs):
            amt += item_need * price[i]
        cache[key] = min(cache[key], amt)
        
    

price = [4,7,9,9,3,2]
special = [[0,0,4,6,2,0,22],[1,4,3,5,5,3,10],[4,5,6,3,4,1,29],[0,3,2,2,4,2,4],[4,6,3,4,4,6,21],[5,6,3,6,3,4,23],[6,1,3,4,6,2,9],[3,3,6,1,5,1,16],[0,3,6,4,0,2,5],[5,1,2,3,5,5,7],[0,1,1,6,2,4,24],[1,5,2,2,6,1,3],[4,2,2,4,3,1,8],[3,1,0,6,1,2,30],[4,6,1,4,0,0,2],[0,4,5,6,2,5,1],[2,6,0,6,6,2,21],[2,1,3,4,0,2,2],[6,4,4,4,1,3,24],[6,3,1,6,5,5,12],[1,3,2,1,3,2,32],[2,2,0,3,1,2,16],[2,4,3,6,6,5,26],[1,6,3,5,0,4,2],[6,2,1,5,6,2,9],[0,4,2,2,5,3,3],[6,3,3,6,0,5,9],[4,3,2,5,3,3,29],[1,6,0,0,1,6,31],[5,6,0,5,4,3,31],[0,4,2,6,0,6,28],[5,4,3,2,5,3,32],[6,5,1,1,4,6,18],[3,3,3,2,3,3,2],[5,6,2,5,3,3,7],[1,2,6,4,4,0,18],[0,4,4,0,0,3,18],[4,2,0,0,3,3,19],[6,0,4,4,4,6,15],[6,2,3,0,2,2,4],[4,1,1,5,5,5,14],[3,6,4,0,6,2,27],[2,4,6,2,2,3,24],[6,0,5,3,1,6,7],[3,1,5,1,2,6,28],[5,2,2,1,1,4,25],[5,6,5,0,3,4,19],[3,5,3,3,5,1,31],[6,0,1,1,6,4,14],[0,3,4,3,3,4,10],[4,1,2,2,0,0,27],[2,2,1,3,5,2,24],[2,3,2,6,1,1,21],[6,6,5,6,2,2,12],[6,6,3,1,0,6,28],[6,4,1,6,5,0,8],[3,3,0,5,4,2,7],[4,3,3,3,0,2,25],[1,2,0,5,2,4,8],[0,1,6,6,5,5,27],[3,6,4,5,2,2,4],[4,4,6,1,5,3,30],[4,3,4,5,5,5,19],[0,0,0,6,1,0,27],[6,5,0,1,2,4,10],[2,6,0,0,1,0,13],[4,1,6,1,4,1,24],[2,4,0,1,4,1,25],[5,1,3,3,4,1,8],[5,5,1,0,2,1,25],[1,6,2,4,0,6,27],[4,0,3,0,5,3,30],[2,4,6,6,3,2,4],[6,4,2,2,0,3,27],[1,2,1,2,2,1,2],[2,0,3,0,5,4,4],[3,5,4,4,1,1,25],[2,1,1,6,3,3,28],[4,4,4,3,6,3,21],[1,4,1,4,2,2,27],[0,6,0,2,2,2,33],[3,3,5,6,4,6,9],[1,0,0,3,4,2,11],[1,3,0,3,0,1,16],[2,3,0,0,0,5,1],[3,5,6,4,1,4,3],[3,1,0,2,6,0,19],[3,0,0,5,3,1,6],[1,0,4,1,2,2,18],[0,0,4,3,5,1,31],[4,4,2,5,5,2,2],[5,0,2,6,5,3,4],[6,2,1,0,2,3,11],[4,5,1,5,3,3,23],[6,2,5,1,6,6,4],[5,6,6,1,5,6,6],[3,2,6,1,4,5,19],[0,2,6,2,5,0,26],[0,1,3,6,3,6,18],[3,5,4,6,5,3,6]]
needs = [6,6,6,6,6,6]
expected = 22

print(Solution().shoppingOffers(price, special, needs))
