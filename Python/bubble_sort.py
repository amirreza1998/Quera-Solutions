###first approach
number = int(input())
sequence = list(map(int, input().split()))

for i in range(number):
    swapped = False
    for j in range(1, number - i):
        if sequence[j - 1] > sequence[j]:
            temp_parmeter = sequence[j]
            sequence[j] = sequence[j - 1]
            sequence[j - 1] = temp_parmeter
            swapped = True
    if swapped == False:
        break
print(*sequence, sep=" ")
# print(" ".join(map(str, sequence)))

###second approach
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j] #intersting code

print(*a, sep=' ')