def longestSubarray(arr):

    myset = set()
    max_list = []
    count    = 0
    prev     = 0

    for i in arr:
        
        if abs(i-prev) <= 1:
            count += 1
            myset.add(i)
        
        if myse




    
    return max(max_list)

# arr = [0,1,2,1,2,4]
arr = [1,1,1,3,3,2,2]
res = longestSubarray(arr)
print('res : ', res)
