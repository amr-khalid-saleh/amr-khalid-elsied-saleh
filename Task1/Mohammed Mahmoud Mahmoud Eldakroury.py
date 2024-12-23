# mohamed mahmoud mahmoud eldakroury
#section : 2 eng nada 
# input : array from user 
#process : compare from sec element with per and ++
#output :sorted array 
#insertion sort algorithm
def insertion_sort(array):
    # Traverse through 0 to len(array)
    for i in range(0, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # set temp element in right position 
        array[j + 1] = temp;

#  User input  size of array
size = int(input("Enter the number of elements in the array: "))
array = []

# input array from user 
for i in range(size):
    element = int(input( "Enter element and press enter to add next: "))
    array.append(element)
    print("Original array:", array)

# Sorting the array using insertion sort
insertion_sort(array)

# Displaying the sorted array
print("Sorted array:", array)
