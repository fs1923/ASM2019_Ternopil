from math import *

n, k = map(int, input().split())
a = list(map(int, input().split()))

op = 0
p = []

for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
            op += 1
            p.append(j)
            if op == k:
                swapped = False
                break
            swapped = True
    if not swapped:
        break

print(op)

for i in range(op):
    print(p[i]+1, p[i]+2)