import random, math, time

#find the "k"th smallest element in array "a" with "n" elements by using Randomized-select in CLRS
def randomized_select(a, n, k):

    def Partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] =  A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def RandomPartition(A, p, r):
        try:
            i = random.randint(p, r)
        except ValueError:
            i = random.randint(r, p)
        A[i], A[r] = A[r], A[i]
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
def  deterministic_select(a, n, k):

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
        for j in range(p, r):
            if A[j] == x: break
            i = i + 1
        A[i], A[r] = A[r], A[i]

        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def Select(lst, p, r, i, group_size = 5):

        n = len(lst)

        # step 1
        if n <= group_size:
            newlst = InsertionSort(lst)
            return newlst[i-1] # <- 배열 start's at 0 index

        # step 2
        group_list = divide(lst, group_size)

        # step 3
        median_list = [findMedian(group) for group in group_list]

        # step 4
        next_i = math.ceil(len(median_list)/2)  # middle guy
        median_of_median = Select(median_list, 0, len(median_list) - 1, next_i)

        # step 5
        q = Partition(lst, p, r, median_of_median)
        k = q - p + 1

        if i < k:
            return Select(lst[p:q], p, len(lst[p:q]) - 1, i)
        elif i == k:
            return lst[q]
        else:
            return Select(lst[q + 1:(r + 1)], 0, len(lst[q + 1:(r + 1)]) - 1 , i - k)

    return Select(a.copy(), 0, (n-1), k)

#check whether the "k"th smallest element in array "a" with "n" elements is the "ans"
def checker(a, n, k, ans):

    def CountingSort(A):
        m = max(A) + 1
        # Create a list K size with initalize value as ZERO
        B = [0]*m   # list holding the results
        C = [0]*m   # list holding the counts
        for j in range(len(A)):     # Couting number of Duplicate values and save to index
            C[A[j]] = C[A[j]] + 1
        for i in range(1, len(C)):       # Create cummulative count
            C[i] = C[i] + C[i-1]
        for j in range((len(A)-1), -1, -1):
            B[C[A[j]]] = A[j]
            C[A[j]] = C[A[j]] - 1
        B.pop(0)
        return B

    lst = a.copy()
    sorted_lst = CountingSort(lst)
    if sorted_lst[k-1] == ans:
        return True
    return False


if __name__ == "__main__":

    time_complexity_dataset = {};

    for i in range(5):
        with open("{0}.txt".format(i)) as file:
            lines = [line for line in file]
            head = lines.pop(0).split()
            time_complexity_dataset[i] = { "n" : int(head[0]), "k" : int(head[1]), "data" : list(map(lambda x : int(x), lines)) }

    for key in time_complexity_dataset:
        dataset             = time_complexity_dataset[key]
        run_time_random     = 0
        run_time_linear     = 0
        test_count          = 10

        for i in range(test_count):
            start_time = time.time()
            a = randomized_select(dataset["data"], dataset["n"], dataset["k"])
            run_time_random = run_time_random + (time.time() - start_time)

            start_time = time.time()
            b = deterministic_select(dataset["data"], dataset["n"], dataset["k"])
            run_time_linear = run_time_linear + (time.time() - start_time)

            status = "correct" if a == b else "incorrect"

            print(i, dataset["n"], a, b, status)

        time_complexity_dataset[key]["time_complexity_random"] = (run_time_random/test_count)
        time_complexity_dataset[key]["time_complexity_linear"] = (run_time_linear/test_count)

    print("number of iteration:", test_count)
    for key in time_complexity_dataset:
        item = time_complexity_dataset[key]
        print(item["n"], item["k"], item["time_complexity_random"], item["time_complexity_linear"])


