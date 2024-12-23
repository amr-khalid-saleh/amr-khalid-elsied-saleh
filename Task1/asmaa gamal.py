#Selection Task

a=[11,2,5,4]
def SelectionSort(array):
    for i in range(len(array)):
        minIndex=i
        for j in range(i+1,len(array)):
            if array[j]< array[minIndex]:
                minIndex=j
        array[i], array[minIndex]=array[minIndex], array[i]
        print(array)
print(SelectionSort(a))
