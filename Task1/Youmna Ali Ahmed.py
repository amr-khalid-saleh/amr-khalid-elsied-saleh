def selection_sort(arr):
    n = len(arr)    
    for i in range(n):       
        min1 = i
        for j in range(i+1, n):
            if arr[j] < arr[min1]:
                min_idx = j               
        arr[i], arr[min_idx] = arr[min1], arr[i]
        print(f"Step {i+1}: {arr}")      
arr = [88, 77, 10, 55, 19]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:",arr)
#section 2
