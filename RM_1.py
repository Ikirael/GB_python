'''
необходимо проверить что открывающие и закрывающие скобки
расставленные верно.
'''
def is_balanced(text):
    open = ["<","(","{","["]
    close = [">",")","}","]"]
    stack = [] 
    for char in text:
        if char in open: 
            stack.append(open.index(char))
        elif char in close: 
            if stack and stack[-1] == close.index(char):
                stack.pop()  
            else:
                return False 
                             
    return (not stack) 

text = input()
if is_balanced(text):
    print ("True")
else:
    print("False")