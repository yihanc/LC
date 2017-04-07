
class Solution(object):
    def buyCake(self, nums, target):
        dp = [ 0 for x in xrange(target + 1)]
        dp[0] = 1
        for i in xrange(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp

if __name__ == "__main__":
    nums = [1, 2, 3]
    for target in xrange(10, 11):
        print(target, Solution().buyCake(nums, target))
