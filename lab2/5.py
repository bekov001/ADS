n = int(input().strip())
names = [input().strip() for _ in range(n)]


unique = []
for name in names:
    if not unique or unique[-1] != name:
        unique.append(name)

unique.reverse()

print(f"All in all: {len(unique)}")
print("Students:")
for name in unique:
    print(name)