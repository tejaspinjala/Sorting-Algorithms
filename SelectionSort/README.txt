Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in 
each iteration and places that element at the beginning of the unsorted list.

Time complexity:
    Best: O(n^2)
    Worst: O(n^2)

Space complexity: O(1)


1) Set the first element as minimum
2) Compare minimum with the second element. If the second element is smaller than minimum, 
    assign the second element as minimum. Compare minimum with the third element. Again, if the 
    third element is smaller, then assign minimum to the third element otherwise do nothing. The 
    process goes on until the last element.
3) After each iteration, minimum is placed in the front of the unsorted list.
4) For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated 
    until all the elements are placed at their correct positions.
