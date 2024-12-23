df selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [24, 29, 82, 92, 81, 60]
selection_sort(arr)
print("Sorted array:")
print(arr)
# section1
