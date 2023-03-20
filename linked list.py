class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def add_ele_at_start(self, head, value):
        new_node = Node(value)
        new_node.next = head
        head = new_node
        return head
    def add_element(self, head, value):
        new_node = Node(value)  #step1 create the new node or new elements
        temp = head
        while temp.next != None:  #step2
            temp = temp.next
        temp.next = new_node     #step3 add the element which you are created
    def remove_element(self, head):
        temp = head
        while temp.next.next != None:  # step1
            temp = temp.next
        temp.next = None              #step2

    def print_list(self, head):
        temp = head
        while temp.next != None:
            print(temp.data, end="->")
            temp = temp.next
            print()

    def search_element(self, value): pass
    def insert(self, head, value, pos):
        new_node = Node(value)
        curr = head
        prev = None
        while pos != 0:
            prev = curr
            curr = curr.next
            pos = pos-1
        prev.next = new_node
        new_node.next = curr
        print()

obj = LinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.add_element(head, 40)
obj.add_element(head, 50)
obj.remove_element(head)
head = obj.add_ele_at_start(head, 50)
obj.print_list(head)
obj.insert(head, 100, 3)
obj.print_list(head)
