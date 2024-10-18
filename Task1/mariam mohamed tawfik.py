#mariam mohmed tawfik
#sec 1 


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        # Find the index of the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")  # Trace the steps
    return arr

# Example usage
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Sorted array:", sorted_array)
