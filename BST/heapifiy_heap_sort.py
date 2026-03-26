def indice_fils_g(i):
    return 2*i + 1 

def indice_fils_d(i):
    return 2*i + 2

def indice_parent(i):
    return (i - 1) // 2

def heapify_max(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        print(f"swap {arr[i]} with {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify_max(arr, n, i)

def heap_sort_max(arr):
    n = len(arr)

    print("Building max heap...")
    build_max_heap(arr)
    print("Max heap:", arr)

    for i in range(n-1, 0, -1):
        print(f"\nMove max {arr[0]} to end")
        arr[0], arr[i] = arr[i], arr[0]

        heapify_max(arr, i, 0)
        print("Heap now:", arr)

    return arr

def heap_sort_max(arr):
    n = len(arr)

    print("Building max heap...")
    build_max_heap(arr)
    print("Max heap:", arr)

    for i in range(n-1, 0, -1):
        print(f"\nMove max {arr[0]} to end")
        arr[0], arr[i] = arr[i], arr[0]

        heapify_max(arr, i, 0)
        print("Heap now:", arr)

    return arr

def heapify_min(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        print(f"swap {arr[i]} with {arr[smallest]}")
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify_min(arr, n, i)

def heap_sort_min(arr):
    n = len(arr)

    print("Building min heap...")
    build_min_heap(arr)
    print("Min heap:", arr)

    for i in range(n-1, 0, -1):
        print(f"\nMove min {arr[0]} to end")
        arr[0], arr[i] = arr[i], arr[0]

        heapify_min(arr, i, 0)
        print("Heap now:", arr)

    return arr

def main():
    arr1 = [4, 10, 3, 5, 1]
    print("Original:", arr1)
    print("Sorted ascending:", heap_sort_max(arr1.copy()))

    print("\n" + "="*40 + "\n")

    arr2 = [4, 10, 3, 5, 1]
    print("Original:", arr2)
    print("Sorted descending:", heap_sort_min(arr2.copy()))

main()