import random, math

#find the "k"th smallest element in array "a" with "n" elements by using Randomized-select in CLRS
def randomized_select(a, n, k):

    def Partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):  # r-1
            if A[j] <= x:
                i = i + 1
                a[i], a[j] =  a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1

    def RandomPartition(A, p, r):
        i = random.randrange(p, r)
        a[i], a[r] = a[r], a[i]
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

    return RandomSelect(a.copy(), 0, (n-1), k)

#find the "k"th smallest element in array "a" with "n" elements by using the worst-case linear-time algorithm in CLRS
def deterministic_select(a, n, k):

    divide = lambda A, s: [ A[i*s : (i+1)*s]   for i in range(math.ceil(len(A)/s)) ]

    def InsertionSort(A):
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i > -1 and A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        return A

    def findMedian(lst):
        sorted_list = InsertionSort(lst)
        middle = math.floor(len(sorted_list) / 2)
        if len(lst) % 2 == 0:
            middle = middle - 1
        return sorted_list[middle]

    def Partition(A, p, r, x):
        i = 0
        for j in range(0, r):
            if A[j] == x: break
            i = i + 1
        A[i], A[r-1] = A[r-1], A[i]

        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r-1] = A[r-1], A[i + 1]
        return i + 1

    def Select(lst, p, r, i, group_size = 5):

        group_list = divide(lst, group_size)
        median_list = [ findMedian(group) for group in group_list ]

        median_of_median = median_list[0] if len(median_list) == 1 else Select(median_list, 0, len(median_list), math.ceil(len(median_list)/2) )
        q = Partition(lst, p, r, median_of_median)
        k = q - p + 1

        if i < k:
            return Select(lst, p, q - 1, i)
        elif i == k:
            return lst[q]
        else:
            return Select(lst, q + 1, r, i - k)

    return Select(a.copy(), 0, n, k)

#check whether the "k"th smallest element in array "a" with "n" elements is the "ans"
def checker(a, n, k, ans):
    lst = a.copy()
    lst.sort()
    if lst[k-1] == ans:
        return True
    return False
