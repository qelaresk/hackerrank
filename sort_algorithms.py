# I'll try to implement all sorted algorithms here - April 2020 under quarantina

def select_sort(L):

    for i in range(len(L)):
        min_index = i
        min_value = L[i]

        for j in range(i+1,len(L)):     
            if min_value > L[j]:
                min_value = L[j]
                min_index = j

            (L[i],L[min_index]) = (L[min_index],L[i])
        print(L)

    return L


def buble_sort(L):

    for i in range(len(L)):
        swap = False
        for j in range(1,len(L)):
            if L[j-1] > L[j]:
                (L[j-1 ], L[j]) = (L[j], L[j-1])
                swap = True

        print(L)
        if swap == False:
            return L

    return L

def comparison(L1, L2):
    L = []
    t = 0
    for i in L1:
        for j in range(t,len(L2)):
            t = j
            if i < L2[j]:
                L.append(i)
                break
            else:
                L.append(L2[j])
    return L

def merge_sort(L):

    return L


if __name__ == '__main__':

    m = [14, 33, 27, 10, 35, 19, 42, 44]

    # m = [14, 33, 27, 35, 10]

    # print('selection sort : ' , select_sort(m))

    # print('buble sort: ' , buble_sort(m))

    L2 = [1, 5, 8, 10]
    L1 = [2, 4, 9, 11]

    print(comparison(L1, L2))

