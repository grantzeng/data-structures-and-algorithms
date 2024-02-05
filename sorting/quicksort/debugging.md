# Debugging my quicksorts
> Why is it broken? Can you reproduce the error?

Try implementing from Wikipedia

What's the array indexing convention? Seems like CLRS vs. the others might be different. Seems sometimes the upper bound is inclusive and sometimes it isn't. So figure out this one first
- To be honest I don't really like the nested while loop version of shifting the two pointers

Use debugger to step through the code (this is a skill you need to learn)

# Need to think about why some of the implementations are broken
There's array indexing problems here.

# I give up for now

Partitioning and array indices for quicksort