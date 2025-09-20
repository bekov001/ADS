from collections import Counter

n = int(input().strip())
arr = list(map(int, input().split()))

cnt = Counter(arr).most_common()
max_freq = cnt[0][1]

modes = [num for num, freq in cnt if freq == max_freq]
modes.sort(reverse=True)

print(*modes)