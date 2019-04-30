def simpleFibonacci(n):
    if n<2:
        return 1
        return simpleFibonacci(n-1) + simpleFibonacci(n-2)

def memoizedFibonacci(n, memory):
    if n<2:
        return 1
    if memory[n] != -1:
        return memory[n]
    memory[n] = memoizedFibonacci(n-1, memory) + memoizedFibonacci(n-2, memory)

def fibonacci(n):
    # memory[i] contains the answer we've already computed for
    # fibonacci(i), where it's -1 if we havent computed it yet
    memory = []
    for i in range(n+1):
        memory += [-1]
    return memoizedFibonacci(n, memory)
