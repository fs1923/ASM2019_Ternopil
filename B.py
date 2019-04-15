n = int(input())

ind = []
nums = list(map(int, input().split()))

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        ind.append(i)
        i+=1

p = len(ind)
cnt = p // 2

if p % 2 != 0:
    cnt+=1

print(cnt)

for i in range(0, p // 2 * 2, 2):
    print(ind[i] + 1, ind[i+1] + 2)
    nums[ind[i]], nums[ind[i+1] + 1] = nums[ind[i+1] + 1], nums[ind[i]]

if p % 2 != 0:
    r = ind[p - 1]
    if r == 0:
        print(2, 3)
    elif r == 1:
        print(1, 2)
    elif r + 2 == len(nums):
        print(len(nums) - 1, len(nums) - 2)
    elif r + 3 == len(nums):
        print(len(nums), len(nums) - 1)
    else:
        j = nums[ind[p - 1] - 1]
        h = nums[ind[p - 1]]
        u = 0
        while nums[u] == j or nums[u] == h:
            u+=1

        print(ind[p - 1] + 1, u + 1)
