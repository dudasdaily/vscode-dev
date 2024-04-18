from DoublyCircularLinkedList import Stack

def is_digit(ch):
    if ord(ch) >= 48 and ord(ch) <= 57:
        return True
    
    else:
        return False

def post_fix(str):
    a = Stack()
    digitPrevious = False

    for i in range(len(str)):
        if is_digit(str[i]):
            if digitPrevious:
                a.push(int(a.pop()) * 10 + int(str[i]))
            
            else:
                a.push(int(str[i]))
                digitPrevious = True
        
        elif str[i] == ' ':
            digitPrevious = False
        
        elif str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
            digitPrevious = False

            if str[i] == '+':
                p1 = a.pop()
                p2 = a.pop()
            
                a.push(p2 + p1)
            
            elif str[i] == '-':
                p1 = a.pop()
                p2 = a.pop()
                a.push(p2 - p1)
            
            elif str[i] == '*':
                p1 = a.pop()
                p2 = a.pop()
                a.push(p2 * p1)
            
            elif str[i] == '/':
                p1 = a.pop()
                p2 = a.pop()
                a.push(p2 / p1)
    
    return a.pop()

str = "700 3 47 + 6 * - 4 /"
a = post_fix(str)

print(a)