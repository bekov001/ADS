import sys
from collections import deque
stack = deque()
for line in sys.stdin:
    line = line.rstrip()
    if line == "!":
        break
    if len(line) >= 3:
        m, num = line.split()
        if m == "+":
            stack.appendleft(int(num))
        elif m == "-":
            stack.append(int(num))
    elif line == "*" and len(stack):
        if len(stack) < 2:
            print(stack.popleft() * 2)
        else:
            print(stack.popleft() + stack.pop())
    elif line == "*" and len(stack) == 0:
        print("error")