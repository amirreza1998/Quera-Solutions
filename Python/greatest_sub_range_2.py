###first approach
import sys
num = int(input())
in_list = list(map(int, input().split(" ")))


ans = -(sys.maxsize - 1)
for left in range(len(in_list) + 1):
    sum = 0
    for right in range(left, len(in_list)):
        sum += in_list[right]

        if ans < sum:
            ans = sum
print(ans)

###second approach
n = int(input())
a = list(map(int, input().split()))
ans = -10 ** 9

for l in range(n):
    s = 0
    for r in range(l, n):
        s += a[r]
        if s > ans:
            ans = s

print(ans)
