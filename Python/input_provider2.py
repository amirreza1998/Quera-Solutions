import sys

input = sys.stdin.read
data = input().split()
data = list(map(int, data))
n,q = data[:2]
a = data[2:n + 2]
query = data[n + 2:]
####-----------in this type of inputting after entering all the input in mac/linux should use ctrl+D-----------####
####-----------and in the windows should use ctrl+Z and enter key-----------####

###---code for write out output in command line---###
sys.stdout.write('\n'.join(map(str, ["this", "is", "results"])) + '\n')
