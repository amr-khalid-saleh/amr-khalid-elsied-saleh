def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # افترض أن العنصر الحالي هو الأصغر
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # تبادل العناصر
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# مثال على الاستخدام
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("الترتيب الناتج:", sorted_array)
