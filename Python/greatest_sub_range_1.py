###first approach
n = int(input())
a = list(map(int, input().split(" ")))

first_try = True
for r in range(0, len(a) + 1):
    for l in range(r):
        if first_try == True:
            result = sum(a[l: r])
            first_try = False
        else:
            result = max(sum(a[l: r]), result)

print(result)

###second approach
n = int(input())
a = [int(x) for x in input().split()]
ans = -10**9
###-------you could use below code for ans instead of specify it hard code---------###
# import sys
# ans = -(sys.maxsize-1)
###-----or you could use below code------###
# ans = float('-inf')

for r in range(1, n + 1):
    for l in range(r):
        s = 0
        for i in range(l, r):
            s += a[i]
        if ans < s:
            ans = s

print(ans)