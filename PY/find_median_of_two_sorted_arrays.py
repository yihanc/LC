__author__ = 'scao'

"""
High Frequency

Median is:
1. find i so that len(m[0:i]) == len((n(i:-1)
2. m[0:i] <= m[[i]

So if two arrays, m and n
m[0, 1, 2 ....... m-2, m-1]
n[0, 1, 2 . ..... n-2, n-1]

assuming we have i and j

m[0 .... i-1]   m[i...... m-1]
n[0 ..... j-1]  n[j...... n -1]

to satisfy (1), hence:
i + j = m - i + n - j
 => j = (m + n) / 2 - i

Assuming m + n is even number, we will address m + n is odd later.

m = [ 0 3, 5, 8 ]
n = [ 2 4 10 12 13 18]

assuming i = 2, m[i]=3, j = 3 ,n[j]=10,

m = [0, 3] , [ 5, 8]
n = [2, 4, 10], [12, 13, 18]

m[i-1] = 3, m[i[ = 5
n[j-1] = 10, n[j] = 12

since m[i] < n[j1], so median must within
[ 5, 8]
[ 2 4 10]

i = 1, j = 1.5

[ 5] [8]
[ 2, 4] [10]




"""