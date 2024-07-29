n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
max_a = max(a)
min_a = min(a)

# list_values = [0]*(max_a - (min_a-(n-1)))


for x in range(min_a - (n - 1) * k, max_a + 1):
    change = 0
    for i in range(1, n + 1): #this is important to start from 1 because otherwise it will start from x-k as first term
        change += abs(x + (i - 1) * k - a[i - 1]) # instead you can use i instead of both i-1 and range(n) but to write
                                                  # exact formule I used i-1 and range(1, n)

    if x == min_a - (n - 1) * k:
        count = change
    elif count > change:
        count = change
print(count)


### second approach
n, k = map(int, input().split())
a = list(map(int, input().split()))

val = 1000 * 1000 * 1000 #you could also do the math.inf or sys.maxsizesys.maxsize

for x in range(-100000, 100000):
    t = 0
    for i in range(n):
        t += abs((x + i * k) - a[i])
    val = min(val, t)

print(val)
