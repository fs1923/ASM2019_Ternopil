n, k = map(int, input().split())

d = dict()

for num in map(int, input().split()):
    if(num in d.keys()):
        d[num] = d[num]+ 1
    else:
        d[num] = 1

n //= 2
for v in d.values():
    if(v > n):
        print('YES')
        break
else:
    print('NO')
