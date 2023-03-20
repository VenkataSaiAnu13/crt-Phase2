class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def add_element(self, head, value):
        new_node = Node(value)  #step1 create the new node or new elements
        temp = head
        while temp.next != None:  #step2
            temp = temp.next
        temp.next = new_node

    def print_list(selfself, head):
        temp = head
        while temp.next != None:
            print(temp.data, end="->")
            temp = temp.next
            print()
    def reverse(self, head):
        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
obj = LinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.add_element(head, 40)
obj.add_element(head, 50)
obj.add_element(head, 60)
obj.add_element(head, 70)
obj.add_element(head, 80)
obj.print_list(head)
head=obj.reverse(head)
obj.print_list(head)


