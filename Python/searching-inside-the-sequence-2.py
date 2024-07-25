# n, q = map(int, input().split(" "))
#
# a = list(map(int, input().split(" ")))
#
# cnt = [0] * max(a)
# # cnt = [0 for _ in range(max(a)+1)]
#
# for item in a:
#     cnt[item - 1] += 1
#
# ps = list(map(lambda _: 0, range(len(cnt))))
# for idx, item in enumerate(cnt):
#     if idx == 0:
#         ps[idx] = item
#     else:
#         ps[idx] = ps[idx - 1] + item
#
# for _ in range(q):
#     x = int(input())
#     if x <= len(ps) + 1:
#         if x != 1:
#             print(ps[x - 2])
#         else:
#             print(0)
#     else:
#         print(ps[len(ps) - 1])


# 2 3
# 1 2
# 1
# 2
# 3

###simpler approach
###instead consider cnt with length of max(a), consider it as length of max(a)+1
n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

cnt = [0] * (max(a)+1)
# cnt = [0 for _ in range(max(a)+1)]

for item in a:
    cnt[item] += 1

ps = list(map(lambda _: 0, range(len(cnt))))
for idx in range(1, len(cnt)):
    item = cnt[idx]
    ps[idx] = ps[idx - 1] + item

for _ in range(q):
    x = int(input())
    if x <= len(ps):
        print(ps[x-1])
    else:
        print(ps[len(ps) - 1])


###use binary search implementation approach





###use bidest default library implementing binary search