This is an implementation of the insertion sort algorithm.

Insertion sort is a simple sorting algorithm that works similar to the way you 
sort playing cards in your hands. We assume that the first card is already sorted then, 
we select an unsorted card. If the unsorted card is greater than the card in hand, it is 
placed on the right otherwise, to the left. In the same way, other unsorted cards are taken 
and put in their right place.

Time Complexity	 
    Best:	O(n + invsersion) # tightly bound by the number of inverstions
    Worst:	O(n2)

Space Complexity:   O(1)

1) The first element in the array is assumed to be sorted. Take the second element and 
    store it separately in key. Compare key with the first element. If the first element 
    is greater than key, then key is placed in front of the first element.

2) Now, the first two elements are sorted.Take the third element and compare it with the 
    elements on the left of it. Placed it just behind the element smaller than it. If there 
    is no element smaller than it, then place it at the beginning of the array.

3) Similarly, place every unsorted element at its correct position.

Worst Case Complexity: O(n2)
    Suppose, an array is in ascending order, and you want to sort it in descending order. 
        In this case, worst case complexity occurs.
    Each element has to be compared with each of the other elements so, for every nth element, 
        (n-1) number of comparisons are made.
    Thus, the total number of comparisons = n*(n-1) ~ n2

Best Case Complexity: O(n)
    When the array is already sorted, the outer loop runs for n number of times whereas the 
    inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.

The insertion sort is used when:
    The array is has a small number of elements
    There are only a few elements left to be sorted

