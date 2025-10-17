def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

n = int(input())
s = input()

vowels = mergesort([c for c in s if c in 'aeiou'])
consonants = mergesort([c for c in s if c not in 'aeiou'])

print(''.join(vowels + consonants))
