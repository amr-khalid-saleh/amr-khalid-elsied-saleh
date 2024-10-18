def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(f"Step {i+1}: {arr}")

arr = [77, 21, 9, 25, 8]
print(arr)
selection_sort(arr)
print("Sorted array:", arr)
#section 2