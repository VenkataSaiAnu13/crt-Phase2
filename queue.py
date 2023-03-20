 open_list=["("]
 close_list=[")"]
def check(myString)
    stack = []
    for i in myString:
        if i in open_list:
            stack.append(i)
        else:
            return unbalanced
        if len(stack)==0
            return balanced
        else:
            return unbalanced
string ="()"
print(string,check(myString))