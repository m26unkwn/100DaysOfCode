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


def reverse_string(string):
    stack=Stack()

    for word in range(len(string)):
        stack.push(string[word])

    reverseString=" "
    while not stack.is_empty():
        reverseString+=stack.pop()

    return reverseString

print(reverse_string("learning Stack"))

