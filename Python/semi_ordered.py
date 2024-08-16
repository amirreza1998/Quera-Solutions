###frist approach with rate of O(n)
number = int(input())
items = list(map(int, input().split(" ")))

count = 0
for idx in range(number):
    if items[idx] != idx + 1:
        count += 1

if count == 2:
    print("YES")
else:
    print("NO")


###second approach with rate of O(n^3)
number = int(input())
items = list(map(int, input().split(" ")))

import copy
for i in range(number):
    for j in range(i):
        p = copy.deepcopy(items)
        a = p[j]
        p[j] = p[i]
        p[i] = a
        sorted_result = 1
        for k in range(1, number):
            if p[k-1] < p[k] :
                sorted_result = 0
                break
        if sorted_result == 1:
            print("YES")
            break
    else:
        continue
    break
else:
    print("NO")


###third approach with rate of O(n)
n = int(input())
a = list(map(int, input().split()))
#count bad numbers
count = 0
for i in range(n):
    if a[i] - 1 != i:
        count = count + 1

if count == 2:
    print('YES')
else:
    print('NO')