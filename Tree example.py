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

    def search(self, root, value):
       if root.data == value:
            return root
       if value < root.data and root.left != None:
            return self.search(root.left, value)
       if value > root.data and root.right != None:
            return self.search(root.right, value)

    def height(self, root):
        if root == None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)
ob = BSTree()
root = Node(10)
ob.add_element(root, 7)
ob.add_element(root, 40)
ob.add_element(root, 5)
ob.add_element(root, 9)
ob.add_element(root, 8)
ob.add_element(root, 15)
ob.add_element(root, 60)
# print(ob.search(root, 15))
# if ob.search(root, 150):
#     print("Element found")
# else:
#     print("Element not found")
print(ob.height(root))




