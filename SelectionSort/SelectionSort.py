def selectionSort(array, size):
   
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[j] < array[min_idx]:
                min_idx = j
         
        # put min at the correct position
        (array[i], array[min_idx]) = (array[min_idx], array[i])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
