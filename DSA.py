# ⚠️ Linked List

'''Created Linked list with basics of class and objects'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Head = Node(10)
Node1 = Node(20)
Node2 = Node("Hi")

Head.next = Node1
Node1.next = Node2

curr = Head
while curr is not None:
    print(curr.data)
    curr = curr.next

print(Head.data, Head.next)
# ---------------------------------------------------------

'''This is main part of Linked List'''


class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data) :
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while (cur.next is not None):
                cur = cur.next
            cur.next = newNode
    def display(self):
        if (self.head is not None):
            cur = self.head
            while (cur is not None):
                print(cur.data, end= " ")
                cur = cur.next
            print()
        else: print("Node is empty.")
    
    def remove(self, target):
        if self.head is None: print("It has no values in it.")
        else:
            if self.head.data == target:
                self.head = self.head.next
            else:
                cur = self.head

                while cur.next is not None and cur.next.data != target:
                    cur = cur.next
                if cur.next is not None:
                    cur.next = cur.next.next
    def search(self, target):
        if self.head is not None:
            cur = self.head
            if self.head.data == target:
                print("Found")
                return 0
            while (cur is not None):
                if cur.data == target:
                    print("Found")
                    return None
                cur = cur.next
            else: print("Not found")
        else: print("Linked list is empty.")


list = LinkedList()
list.add(10)           
list.add(15)           
list.add("Hi")     
list.add(11)     
list.display()      
list.remove(15)
list.remove("Hi")
list.display()
list.search(15) # End