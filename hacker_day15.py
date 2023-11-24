class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        print('head in class: ', head)
        if head == None:            
            head = Node(data)
            # print('head.next: ', head.next)
            # print('head.data: ', head.data)
        else:
            point = head
            # head.next = Node(data)
            while point:
                if point.next == None:
                    point.next = Node(data)
                    return head
                point = point.next


        return head
        


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    print('head in for: ', head)
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head); 	  