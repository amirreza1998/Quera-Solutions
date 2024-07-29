n, q = map(int, input().split(" "))

a = list(map(int, input().split(" ")))

cnt = [0] * max(a)
# cnt = [0 for _ in range(max(a)+1)]

for item in a:
    cnt[item - 1] += 1

ps = list(map(lambda _: 0, range(len(cnt))))
for idx, item in enumerate(cnt):
    if idx == 0:
        ps[idx] = item
    else:
        ps[idx] = ps[idx - 1] + item

for _ in range(q):
    x = int(input())
    if x <= len(ps) + 1:
        if x != 1:
            print(ps[x - 2])
        else:
            print(0)
    else:
        print(ps[len(ps) - 1])


# ###simpler approach
# ###instead consider cnt with length of max(a), consider it as length of max(a)+1
n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

cnt = [0] * (max(a) + 1)
# cnt = [0 for _ in range(max(a)+1)]

for item in a:
    cnt[item] += 1

ps = list(map(lambda _: 0, range(len(cnt))))
for idx in range(1, len(cnt)):
    item = cnt[idx]
    ps[idx] = ps[idx - 1] + item

for _ in range(q):
    x = int(input())
    if x <= len(q):
        print(ps[x - 1])
    else:
        print(ps[len(ps) - 1])


###use binary search implementation approach
n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

a.sort() #it is important to use sorted list in this algorithm
right = len(a) - 1
left = 0
for _ in range(q):
    query = int(input())
    while right >= left:
        mid = (right + left) // 2
        if a[mid] == query:
            while a[mid-1] == a[mid]:
                mid -= 1
            print(mid)
            break
        elif a[mid] > query:
            right = mid-1
        elif a[mid] < query:
            left = mid+1
    else:
        if query>max(a):
            print(len(a))
        else:
            print("error in giving input")


###use binary search implementation approach recursive
def binary_search(array, right, left, x):
    while right >= left:
        mid = (right + left) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, mid - 1, left, x)
        elif array[mid] < x:
             return binary_search(array, right, mid + 1, x)
    return len(array)


n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
a.sort()
for _ in range(q):
    print(binary_search(a, len(a)-1, 0, input()))


###use bidest default library implementing binary search
import bisect
import sys

n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

a.sort()
for i in range(q):
    print(
        bisect.bisect_left(
            a, int(input())
        )  # it is important to give sorted list to the bisect
    )
