VEBTree
=======

An implementation of a Van Emde Boas Tree written in Python.

A Van Emde Boas Tree is a data structure for unique integers. It supports the operations:

- Insert
- Check for membership
- Predecesors
- Successors
- Minimum
- Maximum
(- Delete not yet implemented)

All operations except for Minimim and Maximum have runtime  O(log(log u)) where u is the universe size (all elements inserted are integers between 0 and u-1). Minimum and Maximum have runtime O(1).
Note that this is much faster than any binary search tree or any other common priority queue. 

This implementation allocates memory dynamically so that it uses O(n) space (where n is the number of elements in the tree). 

## Dependencies
None.

## Usage

To create a Van Emde Boas tree, choose an approximate universe size.

```python
>>> from VEB import VEB
>>> u = 10000
>>> veb = VEB(u)
```

 Based on these preferences, a Van Emde Boas tree will be created that can handle the universe size specified.
 NOTE: Actually, the Van Emde Boas tree will usually have capacity a lot higher than the universe size you specified.
 In fact, the capacity of the Van Emde Boas tree will be the lowest number of the form 2^2^2^...^2 that is greater than u. 
 In this specific case, the actual capacity of the Van Emde Boas tree can be checked by doing:

```python
>>> veb.u
65536
```

 Since 2^2^2^2^2 = 65536. This is a lot higher than 10000, but it makes the implementation much more elegant and since the space isn't allocated
 dynamically, its not much harm to the user on the predecessor, successor and membership operations. Only an additive constant factor slowdown in the runtime. The insert might have a more significant slowdown (more on this on the Improvements section).

```python
>>> veb.insert(100)
>>> veb.insert(123)
>>> veb.insert(2)
```

 You now inserted 100, 123, and 2. You can check membership of elements.

```python
>>> veb.member(2)
True
>>> veb.member(124)
False
```

 You can check predecessors and successors. Note that the predecessor of the lowest elements returns None. Likewise, the successor of the biggest
 element return None.

```python
>>> veb.predecessor(100)
2
>>> veb.predecessor(123)
100
>>> veb.predecessor(2)
>>> veb.successor(100)
123
>>> veb.successor(99)
100
>>> veb.successor(120)
123
```
 The minimum and maximum elements are stored in fields min and max.

```python
>>> veb.min
2
>>> veb.max
123
``` 

## Performance

I tested the speed for performing all operations on all elements of the Van Emde Boas tree, so the time is amortized for all elements.

```
Creating VEB Tree for 50000 elements...
Speed per insertion: 0.000032 seconds
Speed per membership query: 0.000013 seconds
Speed per predecessor query: 0.000026 seconds
Speed per successor query: 0.000025 seconds
```

## Improvement

 I did not do any tricks to boost performance. There might be some bit-tricks worth using for lowering the time even more. Also, the tree currently cannot delete elements. It might be worth trying to make the capacity of the Van Emde Boas tree match more closely the capacity specified by the user. 

 The one point of improvement by taking that approach would be lowering the time it takes to initialize the clusters. Since a list is created of size sqrt(u). Suppose for example that we create 

```python
>>> veb = VEB(65537)
```

 Here we have the user-specified capacity 65537 = 2^2^2^2^2 + 1. Therefore, the Van Emde Boas tree will have actual capacity of 65537^2. Which means that the top level of the tree will have a list of 65537 "clusters", which is a massive overkill, and although most will be empty and specified to None, the initialization of the list takes much longer than needed. I tried having the clusters saved in a dictionary to avoid making the long lists, and while the insertions took about 60% of the time, membership took significantly longer.