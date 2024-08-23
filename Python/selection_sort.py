### first approach
number = int(input())
sequence = list(map(int, input().split()))

for i in range(number - 1):
    min_index = i
    for j in range(i, number):
        if sequence[j] < sequence[min_index]:
            min_index = j
    sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
print(*sequence, sep=" ")

### second approach
### in this approach reversly sort base on the max instead of min
number = int(input())
sequence = list(map(int, input().split()))


for i in range(number - 1):
    max_index = 0
    for j in range(number - i):
        if sequence[j] > sequence[max_index]:
            max_index = j
    sequence[max_index], sequence[number - i - 1] = sequence[number - i - 1], sequence[max_index]
    # print(i)
print(*sequence)



###third approach
### min(..., key=...) function evaluates the iterable produced by range and uses the values obtained from the lambda
### function to find the minimum value. Instead of returning the minimum value itself, it returns the index of that minimum value.
n = int(input())
a_seq = list(map(int, input().split()))
for i in range(n - 1):
    min_index = min(range(i, n), key=lambda x: a_seq[x])
    a_seq[i], a_seq[min_index] = a_seq[min_index], a_seq[i]
print(*a_seq, sep=" ")