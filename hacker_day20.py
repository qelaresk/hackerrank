import sys

a = list(map(int, input().strip().split(' ')))

total_swap = 0
swap = True

for i in a:
    for j in range(1,len(a)):
        if a[j-1] > a[j]:
            (a[j-1],a[j]) = (a[j],a[j-1])
            total_swap += 1
            swap = False
    
    if swap:
        break

print('Array is sorted in {} swaps. '.format(total_swap))
print('First Element: {} '.format(a[0]))
print('Last Element: {}'.format(a[-1]))

        