#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) = run time here will grow at an equal rate to an increasing input n.


b) 0(n^2) = The first loop has n iterations, and the inner loop has J*2 iteratinos for each outer loop iteration. Inner loop iterations are thus: 1 * 2 * 4 * 8 * ... n, which becomes n(n*2)/2. When simplified, this is n^2 + 2, but we can eliminiate constant 2. 


c) O(n) = This is a recursive function, which is characterized as 0(n). 

## Exercise II

Per the question, you want to minimize the the number of broken eggs - to do so, you have to reduce the number of eggs dropped, as well. 

Our goal here is to find what f is, and so we can treat the building as a sorted array (as floors would be "sorted" at this point). 

Binary searches are useful when you want to serach for a single element (in this case, floor f) in a sorted array. As mentioned, we can assume that the "array" is sorted, and thus, the time complexity of a binary search would be 0(logn) in this instance. 

We could start out by dividing the length or the array, or the building size, in half. Then, we can start with the middle index. 

If the egg breaks when dropped from the middle, then we can eliminate the right hand side of the array, because now we're trying to go to a lower floor to find out where it starts breaking. If the egg doesn't break, we can eliminate the left hand side. Either way, we can continue this process until we find the value of f. 
