import heapq


q, k = map(int, input().split())

h = []
heapq.heapify(h)


total = 0
for _ in range(q):
    command = input()
    if command == "print":
        print(total)

    else:
        c, n = command.split()
        n = int(n)

        if len(h) <k:
            heapq.heappush(h, n)
            total += n
        else:
            value = h[0]
            if n > value:
                total += n - value
                heapq.heapreplace(h, n)


