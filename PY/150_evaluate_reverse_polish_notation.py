# 150. Evaluate Reverse Polish Notation   QuestionEditorial Solution  My Submissions
# Total Accepted: 78559
# Total Submissions: 308384
# Difficulty: Medium
# Contributors: Admin
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# 
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# Subscribe to see which companies asked this question
from collections import deque
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        d = deque()
        for i in xrange(len(tokens)):
            print(d)
            char = tokens[i]
            if char not in "+-*/":      # str can be negative or others
                d.append(int(char))
                continue
            else:
                y = d.pop()             # Note that first pop y, then pop x
                x = d.pop()
                if char == "+":
                    d.append(x + y)
                elif char == "-":
                    d.append(x - y)
                elif char == "*":
                    d.append(x * y)
                else:
                    d.append(int(float(x) / y)) # 6 / -132 = -1 in PY but = 0 in java
                    #d.append(x // y)        # Java
        
        return d.pop()

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print("result : " , Solution().evalRPN(tokens))
