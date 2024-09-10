import sys
sys.setrecursionlimit(100000000)

n = int(input())


def recursive(n):
    if n == 0:
        return 5

    recursive_result = recursive(n - 1)
    if n % 2 == 0:
        return recursive_result - 21
    else:
        return recursive_result * recursive_result


print(recursive(n))
