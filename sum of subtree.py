class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
class BSTree:
    def add_element(self, root, value):    #this approach is called recursive approach
       new_node = Node(value)
       if new_node.data < root.data:
           if root.left != None:
               self.add_element(root.left, value)
               return
           else:
                root.left = new_node
                return
       else:
           if root.right !=None:
               self.add_element(root.right, value)
           else:
               root.right = new_node
    def sum(self, root):
        sum = root.data
        if root.left != None:
            sum += self.sum(root.left)
        if root.right != None:
            sum += self.sum(root.right)
        return sum
ob = BSTree()
root = Node(10)
ob.add_element(root, 7)
ob.add_element(root, 40)
ob.add_element(root, 5)
ob.add_element(root, 9)
ob.add_element(root, 15)
ob.add_element(root, 60)
print(ob.sum(root.left))
print(ob.sum(root.right))
