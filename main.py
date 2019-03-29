from hw1 import *

if __name__=="__main__":

    for i in range(100):

        a = list(set([random.randint(1, 1000000) for i in range(1000000)]))
        n = len(a)

        k = random.randint(1, n - 1)
        random.shuffle(a)

        ans1 = randomized_select(a, n, k)
        if checker(a, n, k, ans1) == True:
            print(i, "correct", k)
        else:
            print(i, 'incorrect =================================================')
        ans2 = deterministic_select(a, n, k)
        if checker(a, n, k, ans2) == True:
            print(i,"correct", k)
        else:
            print(i, 'incorrect =================================================')

    print("All Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    '''
    a = [ 4, 5, 1, 3, 6, 7, 9, 10, 2, 8 ]
    n = 10
    k = 4
    ans1 = randomized_select(a, n, k)
    if checker(a, n, k, ans1)==True:
        print('correct')
    else:
        print('incorrect')
    ans2 = deterministic_select(a, n, k)
    if checker(a, n, k, ans2)==True:
        print('correct')
    else:
        print('incorrect')
    '''