#section ( 1 )  rola awad dweek

numbers=[4 , 3 , 9 , 6 , 2]
for i in range(len(numbers)):
    min_index=i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
print(numbers)


