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



####-----------------use IO.StringIO for write you input to the input function-------------------###
import sys
from io import StringIO
sys.stdin = StringIO("""5
1 2 3 4 5
223232 23 23""")
print(input())
print(f"the second:{input()}")