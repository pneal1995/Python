def gaussianElimination(A, b):
    n = len(A)
    x = [0]*n
    for k in range(n):
        # try to make the kth row of A only have entries from k onward
        # but first, find a row that has some non-zero entry in the
        # kth column, and swap it to make it the kth row
        pivot = k;
        for i in range(k, n):
            if A[i][k] != 0:
                pivot = i
                break
        if pivot != k:
            b[k],b[pivot] = b[pivot],b[k]
            for i in range(k, n):
                A[k][i],A[pivot][i] = A[pivot][i],A[k][i]
            # now change the ith row of A to zero out its kth column by
            # adding a multiple of the kth row to it
            for i in range(k+1, n):
                factor = -A[i][k] / A[k][k]
                b[i] = b[i] + factor*b[k]
                for j in range(k, n):
                    A[i][j] = A[i][j] + factor * A[k][j]
        # now A is diagonal and its easy to solve for x
        for ii in range(n):
            i = n - ii - 1
            x[i] = b[i]
            for j in range(i+1, n):
                x[i] = x[i] - A[i][j]*x[j]
            x[i] = x[i] / A[i][i]
        return x