# if we can't make change for n cents using L, returns -2
def simpleMakeChange(n, L):
    if n==0:
        return 0
    # if possible to make change for n, the answer is definitely less
    # than n + 1
    answer = n + 1
    for x in L:
        if x <= n:
            val = simpleMakeChange(n-x, L)
            if val != -2:
                answer = min(answer, 1 + val)
        if answer == n + 1:
            answer = -2
        return answer

def memoizedMakeChange(n, L, memory):
    if n==0:
        return 0
    if memory[n] != -1:
        return memory[n]
    # if possible to make change for n, the answer is definitely less
    # than n + 1
    answer = n + 1
    for x in L:
        if x<= n:
            val = memoizedMakeChange(n-x, L, memory)
            if val != -2:
                answer = min(answer, 1 + val)
    if answer == n + 1:
        answer = -2
    memory[n] = answer
    return memory[n]

# if we can't make change for n cents using L, returns -2
def makeChange(n, L):
    # memory[i] contains the answer we've already computed to
    # make change for i cents, where its -1 if we haven't computed it
    # yet. if we can't make change for n cents, we put -2 as the value
    memory = []
    for i in range(n+1):
        memory += [-1]
    return memoizedMakeChange(n, L, memory)

print(makeChange(95, [1, 2, 6, 10, 12, 25]))