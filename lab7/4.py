from collections import deque
from itertools import  islice


def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # print(mid)
    left = deque(islice(arr, 0, mid))
    right = deque(islice(arr, mid, len(arr)))
    return merge(mergesort(left, key), mergesort(right, key), key)


def merge(left, right, key):
    left = deque(left)
    right = deque(right)
    result = []
    while left and right:
        if key(left[0]) < key(right[0]):
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    result.extend(left)
    result.extend(right)
    return result

scale = {
    'A+': 4.00, 'A': 3.75,
    'B+': 3.50, 'B': 3.00,
    'C+': 2.50, 'C': 2.00,
    'D+': 1.50, 'D': 1.00,
    'F': 0.00
}

n = int(input())
students = []

for _ in range(n):
    data = input().split()
    lastname, firstname = data[0], data[1]
    subj_count = int(data[2])
    items = data[3:]

    total_points, total_credits = 0, 0
    for i in range(0, subj_count * 2, 2):
        grade = items[i]
        credits = int(items[i + 1])
        total_points += scale[grade] * credits
        total_credits += credits

    gpa = total_points / total_credits if total_credits > 0 else 0
    students.append((gpa, lastname, firstname))


students = mergesort(students, key=lambda x: (x[0], x[1], x[2]))

for gpa, last, first in students:
    print(f"{last} {first} {gpa:.3f}")
