def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Step {i+1}: {arr}")

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
#           صلاح عبد الحكيم محمد الناهي 
#                     سشكن 3 
#                 م/احمد الديموكسي  
