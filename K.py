from math import *

n, m, k = map(int, input().split())
a, b, c = map(int, input().split())

sb = b/m
mb = c/k/m

sb_o = sb < a
mb_o = False

if(sb_o):
    mb_o = mb < sb
else:
    mb_o = mb < a


price = 0
if mb_o:
    t = n // k
    n %= k
    price += t * c

if(sb_o):
    price += n*b
else:
    price += a*m*n

print(price)
