This is an implementation of the bubble sort algorithm.

Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

Given a list of elements, we sort them in ascending order.

Time complexity:
    Best: O(n)
    Worst: O(n^2)

Space complexity: O(1)

1)First Iteration (Compare and Swap)
    1. Starting from the first index, compare the first and the second elements.
    2. If the first element is greater than the second element, they are swapped.
    3. Now, compare the second and the third elements. Swap them if they are not in order.
    4. The above process goes on until the last element

2) Remaining Iteration
    The same process goes on for the remaining iterations.
    After each iteration, the largest element among the unsorted elements is placed at the end. 