def popularNToys(numToys, topToys, toys, numQuotes, quotes):

    my_dict ={}
    toys.sort()

    print('toys: ',toys)

    for i in toys:
        for j in quotes:
            if i.lower() in j.lower():
                my_dict[i] = my_dict.get(i,0) + 1

    top_list =[]
    i = 0
    
    for w in sorted(my_dict, key=my_dict.get, reverse=True):
        top_list.append(w)
        i += 1
        if topToys == i:
            break
        
        
    


            

    print('my_dict  : ', my_dict)
    print('top_list : ', top_list)



toys   = ['elmo','elsa','legos','drone','tablet','warcraft','tick']
quotes = ['Elmo ashdjksahd. Elmo asdshjad','the nnew Elmo ashdhjsa', 'Elsa asjdhjkashd. Elsa sbdhsjd', 'Elsa asjdhjkashd. Elsa sbdhsjd','Elsa asjdhjkashd. Elsa sbdhsjd','legos skjahdjkshd','tablet asdghjsd','warcraft ajshdghjsg']
popularNToys(6,3,toys,6,quotes)