#section 1
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Step {i+1}: {arr}")


arr = [67, 29, 15, 22, 14]
print(arr)
selection_sort(arr)
print(arr)
