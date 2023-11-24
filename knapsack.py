import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    my_list = []

    for i in arr:
        sum = 0
        j = 1
        while True:
            sum = i*j
            if sum == k:
                return k
            elif sum < k:
                my_list.append(sum)
            else:
                break
            j += 1

    print('first my_list : ', my_list)

    num_counter1 = 0
    num_counter2 = 0
    sum = 0
    for i in range(len(my_list)):
        num_counter1 += 1
        # print('len my_list: ', len(my_list))
        if k % my_list[i] == 0:
            my_list.append(k)
        for j in range(len(my_list)):
            num_counter2 += 1
            sum = my_list[i] + my_list[j]
            if sum == k:
                my_list.append(sum)
            elif sum < k:
                my_list.append(sum)
            else:
                continue

    
    print('second my_list : ', my_list)
    print('num counter1 : ', num_counter1)
    print('num counter2 : ', num_counter2)

    if len(my_list) == 0:
        return 0
    return max(my_list)



        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # nk = input().split()

    # n = int(nk[0])

    k = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = unboundedKnapsack(k, arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()