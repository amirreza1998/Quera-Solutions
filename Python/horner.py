import sys

sys.setrecursionlimit(1000000)

n, x = list(map(int, input().split(" ")))
a_i = list(map(int, input().split(" ")))

### 5 * (5 * (2) -3) + 1
### 2(2+2)+3

### first approach (recursive)
def recursive(a_i, x, n):

    if n == 0:
        return a_i[0]

    recursive_result = recursive(a_i, x, n -1)
    return ((x * recursive_result) + a_i[n]) %1000000007
print(recursive(a_i, x, n)%1000000007)

### second approach (loop)
P = 0
for i in range(n + 1):
    P = (P * x + a_i[i]) % 1000000007
print(P)

