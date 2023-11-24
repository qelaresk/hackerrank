
def minion_game(string):
    s_score = 0
    k_score = 0

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            k_score += len(string) - i
        else:
            s_score += len(string) - i

    if s_score > k_score:
        print('Stuart' + ' ' + str(s_score))
    elif k_score > s_score:
        print('Kevin' + ' ' + str(k_score))
    else:
        print('Draw')

        


if __name__ == '__main__':
    s = input()
    minion_game(s)