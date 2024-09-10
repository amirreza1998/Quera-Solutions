import math

x = int(input())

### first approach
def recursive(x):
    if x // 10 == 0:
        return x

    return recursive(x // 10) + x % 10

print(recursive(x))


### second approach
sumation = 0
recursive_range = int(math.log10(x))
for i in range(recursive_range + 1):
    if x < 10:
        sumation += x
    else:
        sumation += x % 10
        x = x // 10

print(sumation)


### third approach
x = input()
print(sum(map(int, list(x))))