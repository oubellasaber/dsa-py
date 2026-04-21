def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def binary_search_recursive(arr, target, l=0, r=None):
    if r is None:
        r = len(arr) - 1

    if l > r:
        return -1

    mid = (l + r) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, r)
    else:
        return binary_search_recursive(arr, target, l, mid - 1)