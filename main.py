from hw1 import *
import pickle

if __name__=="__main__":

    # with open("ff.bin", 'rb') as pickle_file:
    #     a = pickle.load(pickle_file)
    #
    #     if len(a):
    #         pass

    for i in range(3000):

        a = list(set([random.randint(1, 1000000000) for i in range(2000000)]))
        # a = list(set([random.randint(1, 200) for i in range(100)]))
        n = len(a)

        k = random.randint(1, n - 1)
        random.shuffle(a)

        ans1 = randomized_select(a, n, k)
        if checker(a, n, k, ans1) == True:
            # print(i, "correct", k)
            pass
        else:
            with open("ff.bin", 'wb') as pickle_file:
                pickle.dump({"k": k, "data": n}, pickle_file)
            print(i, 'incorrect =================================================')
            break
        ans2 = deterministic_select(a, n, k)
        if checker(a, n, k, ans2) == True:
            # print(i,"correct", k)
            pass
        else:
            with open("ff.bin", 'wb') as pickle_file:
                pickle.dump({"k": k, "data": n}, pickle_file)
            print(i, 'incorrect =================================================')
            break

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