/* 
1. Two Sum
DescriptionHintsSubmissionsDiscussSolution
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

# 2018.03.30

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var mp = Map[Int, Int]()
        var i = 0
        while (i < nums.size) {
            if (mp.contains(target - nums(i))) {
                return Array[Int](mp(target - nums(i)), i)
            }
            else {
                mp += (nums(i)  -> i)
            }
                
            i += 1
        }
        Array[Int]()
        
    }
}
