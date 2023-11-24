#  to understand heap data structure

import heapq

# def my_delete(h,wanted):

#     for i in range(len(h)):
#         if h[i] = wanted:
#             heapq.heappop(h)
#             return
#         elif h[2*i+1] >= wanted:
#             my_delete(h[2*i+1:],wanted)
#         elif h[2*n+2] >= wanted:





def my_heap():

    a = int(input('take number as a loop : '))
    h = []

    for i in range(a):

        s = list(map(int,input().split(' ')))

        if s[0] == 1:
            heapq.heappush(h,s[1])
        elif s[0] == 2:
            index_of_item = h.index(s[1])               
            print('index: ', index_of_item)
            print('before deleting item :', h)
            (h[index_of_item],h[-1]) = (h[-1],h[index_of_item])
            print('swap h : ', h)
            del h[-1]
            print('remove item: ', h)
            heapq.heapify(h)
            heapq._siftdown()

            # for i in range(len(h)):                // second refactor
            #     if h[i] == s[1]:
            #         print('before deleting item :', h)
            #         (h[i],h[-1]) = (h[-1],h[i])
            #         print('swap h : ', h)
            #         del h[-1]
            #         print('remove item: ', h)
            #         heapq.heapify(h)
            #         break
        #     if(h[0]==s[1]):
        #         h.remove(s[1])
        #         heapq.heapify(h)
        #     else:
        #         h.remove(s[1])
        elif s[0] == 3:
            print(min(h))

    print('heap : ', h)

my_heap()

