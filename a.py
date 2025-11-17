import math


a = int(input())


def get_s(n):
    # k = math.floor(math.log(n + 1, 2))

    k = len(str(bin(n + 1))) - 3
    # print(k)
    s = pow(2, k) - 1
    return s


for i in range(a):
    n = int(input())



    # s = get_s(n)
    t = 0
    while n > 0:
        n -= get_s(n)
        t +=1
    print(t - 1)