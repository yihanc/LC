def gcd2(n1, n2):
    if n1 < n2: n1, n2 = n2, n1
    for i in xrange(n2, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

import random
if __name__ == "__main__":
    n1 = random.randint(10, 50)
    n2 = random.randint(10, 50)
    print(n1, n2, " ", gcd2(n1, n2))
    
