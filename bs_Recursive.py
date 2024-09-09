#binary search recursiv exanakov
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search_recursive(ls, target, start, end):
    if end < start:
        return -1

    pivot = (start + end) // 2

    if ls[pivot] == target:
        return pivot
    elif ls[pivot] > target:
        return binary_search_recursive(ls, target, start, pivot - 1)
    else:
        return binary_search_recursive(ls, target, pivot + 1, end)


print(binary_search_recursive(ls, 4, 0, len(ls) - 1))