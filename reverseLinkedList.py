class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def reverse(self,head):
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
obj.remove_element(head)
head = obj.add_ele_at_start(head, 50)
obj.print_list(head)
head = obj.reverse(head)
obj.print_list(head)




