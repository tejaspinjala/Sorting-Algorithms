def bubblesort(array):
    # loop through the entire array
    for i in range(len(array)):
        # keep track of swapping
        swap = False

        # loop to compare array elements
        for j in range(0, len(array) - 1):
            # compare two adjacent elements
            # change > to < to sort decending order
            if array[j] < array[j + 1]:
                # swapping happens if they are not in
                # the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swap = True

        # if not swapped means that array is already sorted
        if not swap:
            break

array = [25, 36 , 12, 0, -2, 9] 
bubblesort(array)
print('Sorted array: ')
print(array)

