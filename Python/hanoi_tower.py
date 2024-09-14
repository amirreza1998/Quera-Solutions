import sys
sys.setrecursionlimit(100000)

# the solution for this question is that you should move n - 1 first disk
# to the help bar with by using destination bar and then move last disk to the destination
# bar which now all the other disk could be located over it because it is biggest disk
# and then by using source bar, we would move n - 1 disks in the help bar to the destination bar
step = 1
def hanoi(src, dst, help, number_disk):
    global step
    if number_disk == 1:
        print(step, src, dst)
        step += 1
    else:
        hanoi(src, help, dst, number_disk - 1)
        print(step, src, dst)
        step += 1
        hanoi(help, dst, src, number_disk - 1)
n = int(input())
hanoi("A", "B", "C", n)