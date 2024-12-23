
def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

num = int(input("Enter the value of num: "))
array = []

print("Enter the elements one by one:")
for _ in range(num):
    element = int(input())
    array.append(element)

selection_sort(array)

print("Sorted array is:")
for element in array:
    print(element)