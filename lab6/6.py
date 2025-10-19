def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergesort(left, key), mergesort(right, key), key)


def merge(left, right, key):
    n, m = len(left), len(right)
    kL = [key(x) for x in left]
    kR = [key(x) for x in right]
    i = j = 0
    res = []
    res_append = res.append

    while i < n and j < m:
        if kL[i] < kR[j]:
            res_append(left[i]); i += 1
        else:
            res_append(right[j]); j += 1
    if i < n:
        res.extend(left[i:])
    if j < m:
        res.extend(right[j:])
    return res


GPA_MAP = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00,
}

def mark_to_gpa(mark: str) -> float:
    return GPA_MAP.get(mark, 0.0)



n = int(input())
students = []

for _ in range(n):
    data = input().split()
    lastname, firstname = data[0], data[1]
    k = int(data[2])
    subjects = data[3:]

    total_credits = 0
    weighted_sum = 0.0
    for i in range(0, 2 * k, 2):
        mark = (subjects[i])
        credit = int(subjects[i + 1])
        gpa = mark_to_gpa(mark)
        weighted_sum += gpa * credit
        total_credits += credit

    overall_gpa = weighted_sum / total_credits if total_credits > 0 else 0
    students.append((lastname, firstname, overall_gpa))


students = mergesort(
    students,
    key=lambda x: (x[2], x[0], x[1])
)


for last, first, g in students:
    print(f"{last} {first} {g:.3f}")
