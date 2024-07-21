n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
for i in range(q):
    x = int(input())
    count = 0
    for item in a:
        if item < x:
            count += 1
    print(count, end="\n")