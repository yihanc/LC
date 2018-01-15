# 282. Expression Add Operators Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 26850
# Total Submissions: 92446
# Difficulty: Hard
# Contributors: Admin
# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
# 
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []

# 2017.03.16 DFS 

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.helper(num, target, res, "", 0, 0, 0)
        return res
    
    def helper(self, nums, target, res, line, start, cur_res, multi):
        print("----- ", start, line, cur_res, multi)
        if start == len(nums) and cur_res == target:
            res.append(line)
            return
        
        for end in xrange(start + 1, len(nums) + 1):
            #print(start, end)
            if nums[start] == "0" and end - start >= 2:    # 0 for 
                break
            number = int(nums[start:end])
            if start == 0:
                self.helper(nums, target, res, str(number), end, number, number)
                continue
            
            self.helper(nums, target, res, line + "+" + str(number), end, cur_res + number, number)
            self.helper(nums, target, res, line + "-" + str(number), end, cur_res - number, number)
            
            self.helper(nums, target, res, line + "*" + str(number), end, cur_res - multi + multi * number, multi * number )
            
num = "3456237490"
target = 9191
print(num, target)
Solution().addOperators(num, target)
