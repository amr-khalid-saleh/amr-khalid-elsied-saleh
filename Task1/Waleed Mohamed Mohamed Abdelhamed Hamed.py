# Waleed Mohamed Mohamed Abdelhamed Hamed -----> Sec 4

# Time Complexity
# Best Case: O(n2)
# Average Case: O(n2)
# Worst Case: O(n2)

# Space Complexity
# O(1) Constant Amount of Space

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    
arr = [23, 13, 12, 22, 9, 0, 15, 49, 25, -1, -2]
selectionSort(arr)
print(arr) # Return Sorted Array
