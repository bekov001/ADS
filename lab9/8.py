import sys


def prefix_function(s: str):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def main():
    s = sys.stdin.readline().strip()
    n = len(s)

    if n < 3:
        print(0)
        return

    pi = prefix_function(s)
    ans = 0

    # длина a и b = k
    for k in range(1, n):
        if 2 * k >= n:
            break
        m = 2 * k
        base = m - pi[m - 1]
        if k % base == 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()