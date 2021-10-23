openS = ["(","["]
closeS = [")","]"]

def parentheses(text):
    stack = []
    for i in text:
        if i in openS:
            stack.append(i)
        elif i in closeS:
            pos = closeS.index(i)
            if ((len(stack) > 0) and (openS[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"

# Driver code
string = '()'
print(string,"-", parentheses(string))

string = '()()()()()()()()()'
print(string,"-", parentheses(string))

string = '([])[]()'
print(string,"-", parentheses(string))

string = ')'
print(string,"-", parentheses(string))

string = '()['
print(string,"-", parentheses(string))

string = '(([))]'
print(string,"-", parentheses(string))

string = '(((((((((((((((((((((((((((((((((('
print(string,"-", parentheses(string))
