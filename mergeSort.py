def mergeSort(L):
    if len(L)<=1:
        return L
    # recursively sort the first half of L and put the result in A, and
    # recursively sort the second half of L and put the result in B
    A = mergeSort(L[0:int(len(L)/2)])
    B = mergeSort(L[int(len(L)/2):])
    xrange = range
    # now merge A and B, and put the result in C
    C = []
    aindex = 0
    bindex = 0
    for i in xrange(len(L)):
        if aindex==len(A):
            C += B[bindex:]
            break
        elif bindex==len(B):
            C += A[aindex:]
            break
        else:
            if A[aindex] < B[bindex]:
                C += A[aindex:]
                aindex += 1
            else:
                C += [B[bindex]]
                bindex += 1
    return C

def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

# Tests
print(f5(mergeSort([1, 2, 3, 4, 10, 5])))