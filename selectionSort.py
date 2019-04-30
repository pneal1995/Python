def selectionSort(L):
    if len(L) == 0:
        return []
    smallest = L[0]
    smallestIndex = 0
    for i in range(1, len(L)): # Could use xrange here
        if L[i] < smallest:
            smallest = L[i]
            smallestIndex = i
    # In Python, a,b = b,a swaps the contents of the variables a,b
    L[0],L[smallestIndex] = L[smallestIndex],L[0]
    return [L[0]] + selectionSort(L[1:])

print(selectionSort([1,2,3,4,5,6,7,23452,234525,23,34242,2,2,33,3]))