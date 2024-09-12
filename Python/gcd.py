import sys
sys.setrecursionlimit(10000000)


### first approach
x, y = list(map(int, input().split()))

def recursion(x, y):
    if y == 0:
        return x

    return recursion(y, x%y)
print(recursion(x, y))

### second approach
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


a, b = [int(x) for x in input().split()]
print(gcd(a, b))

### third approach
x, y = list(map(int, input().split()))

while True:
    if y != 0 and x != 0:
        if y > x:
            z = y%x
            y = z
        else:
            z = x%y
            x = y
            y = z
    else:
        [print(x) if y == 0 else print(y)]
        break


### forth approach
a, b = [int(x) for x in input().split()]

while b != 0:
    a, b = b, a % b
print(a)