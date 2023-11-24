
def ftest():

    count = 0
    temp_count = 0
    str_n = ''
    
    while(n > 0):
        str_n += str(n%2)
        n = n//2


    for i in str_n:

        if i == '1':
            count += 1
            continue
        else:
            if temp_count < count:
                temp_count = count
            count      = 0

    if count > temp_count:
        return count
    else:
        return temp_count



print(ftest())
