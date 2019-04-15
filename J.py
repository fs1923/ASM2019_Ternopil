n,k = map(int, input().split())

a = 'A'*k

c = 'B'
for i in range(n - k):
    a += c

    if c == 'B':
        c = 'C'
    elif c == 'C':
        c = 'D'
    else:
        c = 'B'

print(a)
