from sys import stdin
from heapq import heappush, heappop

heap = []
item_lookup = set()

def push(v):
    heappush(heap, v)
    item_lookup.add(v)
    print('heap        : ', heap)
    print('item_lookup : ', item_lookup)
    
def discard(v):
    item_lookup.discard(v)
    print('heap        : ', heap)
    print('item discard: ', item_lookup)
    

def print_min():
    while heap[0] not in item_lookup:
        print('heap        : ', heap)
        print('item print: ', item_lookup)
        heappop(heap)
        print('heap        : ', heap)
    
    print(heap[0])
    
# cmds = {
#     1: push,
#     2: discard,
#     3: print_min
# }

n = int(stdin.readline())
for _ in range(n):
    s = list(map(int,input().split(' ')))
    if s[0] == 1:
        push(s[1])
    elif s[0] == 2:
        discard(s[1])
    elif s[0] == 3:
        print_min()