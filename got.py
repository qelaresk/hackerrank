def criticalRouters(numRouters, numLinks, links):

    my_dict  = {}

    for i in range(1,numLinks+1):
        for j in links:
            if i in j:
                my_dict[i]  = my_dict.get(i,0) + 1
                
    
    router_list = []
    temp = 0
    for w in sorted(my_dict, key=my_dict.get, reverse=True):
        if my_dict[w] >= temp:
            router_list.append(w)
            temp = my_dict[w]

    print(router_list)



link = [[1,2],[1,3],[2,4],[3,4],[3,6],[6,7],[4,5]]
criticalRouters(7,7,link)