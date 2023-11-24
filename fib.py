def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        num_counter1 += 1
        return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    if n in my_dict:
        return my_dict[n]
    else:
        num_counter2 += 1
        res = fib(n-1) + fib(n-2)
        my_dict[n] = res
        # print(my_dict)
        return res



if __name__ == "__main__":


    my_dict = {0 : 1, 1:1}
    n = int(input())
    num_counter1 = 0
    num_counter2 = 0
    print(fibonacci(n))
    print(fib(n))
    print('num counter 1: ', num_counter1)
    print('num counter 2: ', num_counter2)










