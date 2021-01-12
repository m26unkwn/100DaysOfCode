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


def base_converter(dec, base):
    digits="0123456789ABCDEF"

    stack=Stack()

    while dec > 0:
        remainder=dec%base
        stack.push(remainder)
        dec=dec//base

    newString=""
    while not stack.is_empty():
        newString= newString +digits[stack.pop()]
        
    return newString


print(base_converter(25, 8))
print(base_converter(26, 26))