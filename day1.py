class Stack:
    arr = []
    size = 5
    def stack_push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def stack_peek(self):
        return self.arr.[-1]
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

s = Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
s.stack_pop()
s.stack_pop()


