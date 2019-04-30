def insertionSort(L):
    for i in range(1, len(L)): # Could use xrange here
        # We assume L[0:i] is already sorted, and now need to put L[i]
        # in its rightful place.
        j = i - 1
        value = L[i]
        while j>=0 and L[j]>value:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = value
    return L