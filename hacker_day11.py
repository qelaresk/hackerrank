if __name__ == '__main__':

    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]

    # sum = 0
    # for i in arr:
    #     sum = 0
    #     for j in i:
    #         sum += j
    #     print('sum: ' , sum)



    # sum = 0 
    # for i in range(0,1):
    #     print('first chapter start ***')
    #     for j in range(0,2):
    #         sum = 0
    #         print('arr[j] : ', arr[j])
    #         for k in range(0,3):
    #             sum += arr[i][k] + arr[i+2][k]
    #             print('a[j][k]     : ' , arr[i][k])
    #             print('arr[j+2][k] : ' , arr[i+2][k])
    #         print('arr[j+2][j+1]   : ' , arr[i+2][i+1])
    #         sum += arr[i+2][i+1]

    #         #     sum += arr[j][k]
    #         #     sum += arr[j+2][k]
    #         # sum += arr[j+1][j+2]
    #         print('sum: ',sum)

    sum_list = []
    sumy = 0 
    for i in range(0,4):
        for k in range(0,4):
            sumy = 0
            for j in range(0,3):
                sumy += arr[i][j+k] + arr[i+2][j+k]
            sumy += arr[i+1][k+1]
            sum_list.append(sumy)

    print(max(sum_list))

        
        



