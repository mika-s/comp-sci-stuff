# Sorting

## Basic principles

### Stability
Stable sorting algorithms maintain the relative order of records with equal keys (i.e., values).

### Method

## Types

### Insertion sort

###### Type: comparison sort

Takes elements from the list one by one and inserts them into the correct position
in the newly sorted list.

###### Space complexity:
- O(n)

###### Time complexity:
- Best:    O(n)
- Average: O(n^2)
- Worst:   O(n^2)

###### Other properties:
- Stable
- Adaptive: efficient for data sets that are already substantially sorted
- Very low overhead

### Selection sort

###### Type: comparison sort

Generally crappy, but with a minimum number of swaps. Good algorithm were
the cost of swapping items is high.

###### Space complexity:
- O(1)

###### Time complexity:
- Best:    O(n^2)
- Average: O(n^2)
- Worst:   O(n^2)

###### Other properties:
- Not stable
- Not adaptive

### Bubble sort

###### Type: comparison sort

Repeatedly steps through the list to be sorted, compares each pair of adjacent
items and swaps them if they are in the wrong order.

Similar properties as insertion sort, but with a higher overhead. Very poor performance
and should not be used in real life.

###### Space complexity:
- O(1)

###### Time complexity:
- Best:    O(n)
- Average: O(n^2)
- Worst:   O(n^2)
        

###### Other properties:
- Stable
- Adaptive: efficient for data sets that are already substantially sorted
