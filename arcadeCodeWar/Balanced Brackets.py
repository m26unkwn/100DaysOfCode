#implementing stack using pyhton class 

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

#Function to check pair
 
def is_match(paren1, paren2):
    if paren1 == "(" and paren2 == ")":
        return True 
    elif paren1 == "{" and paren2 == "}":
        return True 
    elif paren1 == "[" and paren2 == "]":
        return True 
    
    else:
        return False

# Function to check a balance is in stack or not

def is_paren_balanced(paren_string):
    stack=Stack()

    is_balanced=True

    for paren in range(len(paren_string)):
        bottom= paren_string[paren]
        if bottom in "({[":
            stack.push(bottom )
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                top=stack.pop()
                if not is_match(top,bottom):
                    is_balanced=False
            
    if is_balanced and stack.is_empty():
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))