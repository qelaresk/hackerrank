def maxValue(w, v, i, aW):
    print('program start: ' + str(i))

    if i == 0:
        if w[i] <= aW:
            print(' **** v[i] ', v[i])
            return v[i]
        else:
            return 0
    without_i = maxValue(w, v, i-1, aW)
    print('after without_i' + ' ' +  str(i) + ' ' + str(without_i))
    
    if w[i] > aW:
        print('check w[i] if greater than aW' + ' ' + str(w[i]))
        return without_i
    else:
        print('calculare with_i' + '  ' +str(i))
        with_i = v[i] + maxValue(w, v, i-1, aW - w[i])
        print('with_i ', with_i)
    
    return max(without_i,with_i)



maxWeight = 5
w = [2, 3, 5]
v = [9, 7, 8]

res = maxValue(w,v, len(v) - 1, maxWeight)

print(res)