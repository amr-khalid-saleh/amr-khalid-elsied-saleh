def sort_selection(lst):
    length = len(lst)
    for index in range(length):
    
        smallest = index
        for scan in range(index + 1, length):
            if lst[scan] < lst[smallest]:
                smallest = scan
    
        lst[index], lst[smallest] = lst[smallest], lst[index]
        print(f"الخطوة {index+1}: {lst}")
    return lst

nums = [29, 10, 14, 37, 13]
print("القائمة الأصلية:", nums)
sort_selection(nums)
