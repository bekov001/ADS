def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps


text = input().strip()
pattern = input().strip()

n, m = len(text), len(pattern)


if m > n:
    print(0)
    print()
    exit()

lps = build_lps(pattern)
ans = []

i = j = 0
while i < n:
    if text[i] == pattern[j]:
        i += 1
        j += 1
        if j == m:
            ans.append(i - m + 1)  # 1-based index
            j = lps[j - 1]
    else:
        if j > 0:
            j = lps[j - 1]
        else:
            i += 1

print(len(ans))
print(*ans)