###first approach
number = int(input())

ordered_pair = []
for c in range(number//2+1):
    for b in range(c, (number - c)//2 + 1): #b would be greater equal to the c
        a = number - c - b
        if b <= a and c + b > a:
            ordered_pair.append(sorted([a, c, b]))
print(len(ordered_pair))

###second approach
n = int(input())
answer = 0

for i in range(1, n + 1):
    for j in range(i, n - i + 1):
        k = n - i - j
        if i + j > k and k >= j:
            answer += 1
print(answer)