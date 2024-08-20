#first approach
n, k = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))

b = list(map(lambda _: 0, a))

for i in range(n):
    b[i] = a[i] - i * k

b = sorted(b)

if len(b) % 2 == 0:
    M = len(b) / 2
else:
    M = (len(b) + 1) / 2
median = b[int(M) - 1]

print(sum([abs(item-b[int(M)-1]) for item in b]))


###second approach
n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    a[i] = a[i] - i * k
    sum = sum + a[i]

a.sort()

psum = 0
ans = -1

for i in range(n):
    temp = (a[i] * i - psum)
    psum = psum + a[i]
    temp = temp + (sum - psum - a[i] * (n - 1 - i))
    if ans == -1 or temp < ans:
        ans = temp

print(ans)
