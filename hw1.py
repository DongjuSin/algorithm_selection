import random

#find the "k"th smallest element in array "a" with "n" elements by using Randomized-select in CLRS
def randomized_select(a, n, k):

    def Partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r): # r-1
            if A[j] <= x:
                i = i + 1
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
        tmp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = tmp
        return i + 1

    def RandomPartition(A, p, r):
        i = random.randrange(p, r)
        tmp = A[r]
        A[r] = A[i]
        A[i] = tmp
        return Partition(A, p, r)

    def RandomSelect(A, p, r, i):
        if p == r:
            return A[r]
        q = RandomPartition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            return RandomSelect(A, p, q-1, i)
        else:
            return RandomSelect(A, q + 1, r, i - k)

    results = RandomSelect(a, 0, (n-1), k)
    return results

#find the "k"th smallest element in array "a" with "n" elements by using the worst-case linear-time algorithm in CLRS
def deterministic_select(a, n, k):
    return 0

#check whether the "k"th smallest element in array "a" with "n" elements is the "ans"
def checker(a, n, k, ans):
    return True
