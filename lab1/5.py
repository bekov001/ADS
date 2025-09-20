from collections import deque

stack1 = deque(map(int, input().split()))
stack2 = deque(map(int, input().split()))
i = 0

while stack1 and stack2 and i < 1_000_000:
    i += 1
    b = stack1.popleft()
    a = stack2.popleft()

    if (b == 0 and a == 9) or (b > a and not (b == 9 and a == 0)):

        stack1.append(b)
        stack1.append(a)
    else:

        stack2.append(b)
        stack2.append(a)

if not stack1:
    print("Nursik", i)
elif not stack2:
    print("Boris", i)
else:
    print("blin nichya")