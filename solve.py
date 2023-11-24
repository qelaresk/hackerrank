#  hacker rank challenge for today - 07.04.2020

def solve(s):
    my_list = list(s.split(' '))

    # if len(my_list) == 1:
    #     return my_list[0][0].upper() + my_list[0][1:]
    # elif len(my_list) > 1:
    #     return my_list[0][0].upper() + my_list[0][1:] + ' ' + my_list[-1][0].upper() + my_list[-1][1:]

    my_string = ''
    for i in my_list:
        my_string += i.capitalize() + ' '

    return my_string
    # if len(my_list) == 1:
    #     return my_list[0].capitalize()
    # elif len(my_list) > 1:
    #     return my_list[0].capitalize() + ' ' + my_list.pop().capitalize() 

result = solve('hello   world  lol')

print(result)