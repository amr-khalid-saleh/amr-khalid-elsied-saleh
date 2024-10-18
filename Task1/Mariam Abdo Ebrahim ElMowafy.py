# مريم عبده ابراهيم الموافى - سكشن 1
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Iteration {i+1}:")
        print(f"Array before iteration: {arr}")
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        print(f"Minimum element found at index {min_idx} with value {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Array after iteration: {arr}\n")
    return arr
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
arr = selection_sort(arr)
print("Sorted array:", arr)
