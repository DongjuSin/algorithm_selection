import random, math, statistics

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

    results = RandomSelect(a, 0, (n-1), k)
    return results

#find the "k"th smallest element in array "a" with "n" elements by using the worst-case linear-time algorithm in CLRS
def deterministic_select(a, n, k):

    group_size = math.floor(n/5)
    median_list = []

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
        middle = math.ceil(len(sorted_list)/2)
        return sorted_list[middle], sorted_list

    def Select(A, p, r, i):
        if p == r:
            return A[p]
        q = Partition(A, p, r)
        k = q - p + 1
        if i < k:
            return Select(A, p, q - 1, i)
        elif i == k:
            return A[q]
        else:
            Select(A, q + 1, r, i - k)

    def Partition(A, p, r, x):

        # search for x in array
        i = 0
        for j in range(0, r):
            if A[j] == x:
                break
            i = i + 1
        tmp = A[i]
        A[i] = A[r]
        A[r] = tmp

        # ==========================

        #x = A[r] <- normal partition, but this time param
        i = p - 1
        for j in range(p, r):  # r-1
            if A[j] <= x:
                i = i + 1
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
        tmp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = tmp
        return i + 1

    while len(a):

        # Step 1:  divide the n elements of the input array into n/5 groups of 5 elements each...
        tmp_list = [a.pop(0)  for i in range(0, group_size)]

        # Step 2: Find th median of each of the groups by first insertion sorting the elements of each group..
        median, sorted_list = findMedian(tmp_list)
        median_list.append(median)

    def kthSmallest(sorted_list, p, r, k):

        # Step 3: Use SELECT recursively to find the median x of the n/5 medians found in step 2...
        median_of_median = Select(sorted_list, p, r, math.ceil(len(sorted_list)/2) )

        # Step 4: Partition the input array around the median-of-medians x using the modified version of Partition...
        position = Partition(sorted_list, p, len(sorted_list), median_of_median)

        # Step 5: if i == k, then return x. Otherwise, use SELECT recursively to find the ith smallest element on the...
        if position == k:
            return sorted_list[position]
        elif position > k:
            return kthSmallest(sorted_list, p, r-1, k)
        else:
            return kthSmallest(sorted_list, p + 1, r, k - position + p)

    return kthSmallest(sorted_list, 0, len(sorted_list), k)

#check whether the "k"th smallest element in array "a" with "n" elements is the "ans"
def checker(a, n, k, ans):
    return True




