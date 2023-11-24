def runningMedian(a):
    b = []
    temp_a = []

    for i in range(len(a)):

        temp_a.append(a[i])
        temp_a.sort()
        print('sorted temp_a : ', temp_a)

        if len(temp_a) % 2 == 0:
            print(temp_a[(i//2):(i//2+2)])
            print(sum(temp_a[(i//2):(i//2+2)])/2)
            print(round(sum(temp_a[(i//2):(i//2+2)])/2,1))
            # print('even temp : ', temp)
            b.append(temp)
        else:
            temp = round(float(temp_a[i//2]),1)
            # print('odd temp : ', temp)
            b.append(temp)
        

    return b


a = [3,4,5,7,6,9,10,1,2,8]

runningMedian(a)