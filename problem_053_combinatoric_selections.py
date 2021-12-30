# requires Python 3.8
from math import comb

count = 0
for n in range(23, 101):
    for r in range(2, 101):
        val = comb(n,r)
        if val > 1000000:
            count+=(n+1-r-r)
            break
    print(n, count)
