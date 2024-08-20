###first approach
n = int(input())

ordred_list = []
ans = 0
for a in range(1, n // 3 + 1):
    upper_bound = (n - 3 * a) // 2
    lower_bound = max(0, n // 2 - (2 * a) + 1)
    ans += upper_bound - lower_bound + 1
print(ans)



###second approach
###this code rate is O(n^2) so it will cause time limit exceeded error
n = int(input())

ordred_list = []
ans = 0
for a in range(1, n//3 + 1):
    upper_bound = (n - 3 * a)//2
    lower_bound = max(0, n//2 - (2 * a) + 1)
    for x in range(lower_bound, upper_bound + 1):
        b = x + a
        c = n - b - a
        ordred_list.append(tuple(sorted([a, b, c])))
print(len(list(set(ordred_list))))