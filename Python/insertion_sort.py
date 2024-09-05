### first approach
n = int(input())
a_i = list(map(int, input().split(" ")))

for i in range(len(a_i)):
    item_num = i
    for j in range(i).__reversed__():
        if a_i[j] > a_i[j + 1]:
            a_i[j + 1], a_i[j] = a_i[j], a_i[j + 1]
        else:
            break
print(*a_i)
# print(' '.join(a))


### second approach
import sys
sys.setrecursionlimit(2000)

def sort(l, n):
    if n == 0:
        return
    sort(l, n - 1)
    p = n - 1
    while p > 0 and a[p] < a[p-1]:
        a[p], a[p - 1] = a[p - 1], a[p]
        p -= 1

n = int(input())
a = list(map(int, input().split()))
sort(a, n)
for x in a:
	print(x, end=' ')