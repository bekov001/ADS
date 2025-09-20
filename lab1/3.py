a, b = (input().split())

stack1 = []

for el in a:
    if el == "#" and stack1:
        stack1.pop()
    else:
        stack1.append(el)

stack2 = []
for el in b:
    if el == "#" and stack2:
        stack2.pop()
    else:
        stack2.append(el)

print("Yes" if stack1 == stack2 else "No")