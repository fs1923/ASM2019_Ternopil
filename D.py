y = int(input())

for i in range(y):
    n,m,k,h = map(int, input().split())
    if (n>=k) and (m >=k) and (k*h >= n + m):
        print('YES')
    else:
        print('NO')