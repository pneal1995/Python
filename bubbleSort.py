def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                swapped = True
    return L
