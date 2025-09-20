s = input()

stack = []

for el in s:
    if not stack or  el != stack[-1]:
        stack.append(el)
    else:
        stack.pop()

print("YES" if not stack else "NO")