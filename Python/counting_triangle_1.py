###first approach
number = int(input())

ordered_pair = []
for c in range(number):
    for b in range(number):
        for a in range(number):
            if a + b + c == number and a <= b <= c and a + b > c:
                ordered_pair.append(sorted([a, c, b]))
print(len(ordered_pair))

###second approach
n = int(input())

ans = 0
for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            if a + b + c == n and a + b > c:
                ans += 1

print(ans)


###third approach
n = int(input())

count = 0
# Iterate through all possible values of a, b, and c
for a in range(1, n // 2 + 1):
    for b in range(a, (n - a) // 2 + 1):
        c = n - a - b
        if c >= b and a + b > c:
            count += 1

print(count)