n = int(input())

data = [int(i) for i in input().split()]
res = []
stack = []
for el in data:
    while stack and stack[-1] > el:
        stack.pop()
    if stack:
        res.append(stack[-1])
        # stack.append(el)
    else:
        res.append(-1)
    stack.append(el)

print(*res)