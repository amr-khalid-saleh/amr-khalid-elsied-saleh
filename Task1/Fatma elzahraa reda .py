def selection_sort(arr):
    n = len(arr)
    for i in range(n):
       
        min_index = i
     
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")
        print(f"Min Index: {min_index}")
        print(f"Swapped {arr[i]} with {arr[min_index]}")
        print("------------------------")

numbers = [3 , 17 , 9 , 33 , 27 , 20 ]
selection_sort(numbers)

#فاطمة الزهراء رضا عبد الفتاح 
# سكشن 2