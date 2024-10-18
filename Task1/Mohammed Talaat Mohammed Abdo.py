def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


numbers = [5, 6, 8, 3, 1, 4, 2, 7]

selection_sort(numbers)
print("Sorted numbers:", numbers)

#section: 5