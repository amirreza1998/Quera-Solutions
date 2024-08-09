###FIRST APPROACH
n = int(input())
a = list(map(int, input().split(" ")))

a.sort()
if len(a)%2 == 0:
    M = len(a)/2
else:
    M = (len(a)+1)/2
# print(M)
print(a[int(M)-1], sum([abs(item-a[int(M)-1]) for item in a]))


###SECOND APPROACH
n = int(input())
a = sorted([int(x) for x in input().split()])

M = a[(n - 1) // 2]
ans = 0
for i in range(n):
    ans += abs(a[i] - M)

print(M, ans)