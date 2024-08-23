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


### The first loop will condition on the value of a. We know that a <= b <= c and a + b + c = n.
### Therefore, a must be <= n/3. (For contradiction proof, suppose a > n/3, in this case a,b,c > n/3,
### so a + b + c = n > n, which is a contradiction.) So the value of a is in the range of 1 to n/3 is located
