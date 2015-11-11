# Sorting

## Basic principles

### Stability

### Method

## Types

### Insertion sort

Takes elements from the list one by one and inserts them into the correct position
in the newly sorted list.

- Stable
- Requires O(1) extra memory space
- O(n^2) comparisons
- O(n^2) swaps
- Adaptive: efficient for data sets that are already substantially sorted
- Very low overhead

### Selection sort

Generally crappy, but with a minimum number of swaps. Good algorithm were
the cost of swapping items is high.

- Not stable
- Requires O(1) extra memory space
- O(n^2) comparisons
- O(n) swaps
- Not adaptive