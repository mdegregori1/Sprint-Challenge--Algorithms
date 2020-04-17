#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a) 0(n) - while the main loop is running at 0(n^3), the inner loop is proportionally increasing at 0(n^2). Therefore, the actual runtime is decrease to 0(n^1), or 0(n). 
b) 0(n)^2 = here, the outside loop is running at a runtime of 0(n), while the inside is runnin at 0(2n). When combined, we get 0(2n^2), or 
0(n)^2, since we don't care about constants. 
c) 0(n) - there is a recursive call that counts down each time, so it will only run n times. 

## Exercise II

Binary Search - 0(log(n))

Think of the building as a vertical list, that is already "sorted" by floor (chronological). 

Since you want to minimize the amount of eggs dropped, you don't want to start at the bottom by doing a linear search - rather, it makes more sense to do a binary search, and start at the middle of the building. 

If you drop an egg from the middle floor, and it breaks, then you can eliminate every floor above it. Likewise, if it doesn't break, you can eliminate any floor below it. 

Imagine that it doesn't break at the midpoint (mid = len(arr) // 2) - you can eliminate everything below mid, and then find a new midpoint from the top half that remains. Continue to do this until you find the first value at which the egg breaks. 