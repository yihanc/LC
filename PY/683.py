# leetcode683，给没有会员的同学贴在这里吧。
# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.. Waral 鍗氬鏈夋洿澶氭枃绔�,
# 
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
# . 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
# For example, flowers = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
# 
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷
# 
# If there isn't such day, output -1.. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
# 
# Example 1:
# Input: . more info on 1point3acres.com
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input: 
# flowers: [1,2,3]-google 1point3acres
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].
# 
# 但是和Leetcode683不同的是，需要返回满足条件的最后一天而不是第一天。. 鍥磋鎴戜滑@1point 3 acres
# 比如：([3,1,5,4,2],1)
# leetcode原题应该返回2，但是变形后应该返回4。原题的解发可以搜Google或者Youtube。变形就稍微改一下就行。. 鍥磋鎴戜滑@1point 3 acres
# 这一题的时间要求O(nlgn)，空间要求O(n)。
