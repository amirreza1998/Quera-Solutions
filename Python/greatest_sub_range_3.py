### first approach
n = int(input())
a_i = list(map(int, input().split(" ")))


ans = a_i[0]
maxsum = a_i[0]
for i in range(1, n):
    maxsum = max(maxsum + a_i[i], a_i[i])
    # print(maxsum)
    ans = max(ans, maxsum)
print(ans)


### second approach
### recursive approach
import sys
sys.setrecursionlimit(1000000)

n = int(input())
a_i = list(map(int, input().split(" ")))


def maxsum(a_i, i):
    if i == 0:
        return a_i[0], a_i[0]

    previous_max, ans = maxsum(a_i, i - 1)
    biggest_with_i_end = max(previous_max + a_i[i], a_i[i])
    ans = max(ans, biggest_with_i_end)  # biggest sum range

    return biggest_with_i_end, ans


_, ans = maxsum(a_i, n - 1)
print(ans)