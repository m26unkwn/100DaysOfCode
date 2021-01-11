class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def convert_int_to_bin(dec_num):
  stack=Stack()
  while dec_num>0:
    remainder=dec_num%2
    stack.push(remainder)
    dec_num=dec_num//2
  bin=""
  while not stack.is_empty():
    bin+=str(stack.pop())
  return bin

print(convert_int_to_bin(242))


