from collections import deque


t = int(input())
for i in range(t):
    n = int(input())



    res =  ["x" for i in range(n)]
    ans  = deque(range(n))


    index = 1
    while len(ans) > 0:
        ans.rotate(-index)
        if res[ans[0]] != "x":
            print(-1)
            break
        res[ans[0]] = index
        ans.popleft()
        index += 1

    else:
        print(*res)