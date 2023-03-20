stack=[]
s=input("enter string:")
for i in s:
    if i == "(":
        stack.append(i)
    elif i == ")" and len(stack) != 0:
        stack.pop()
    else:
        print("invalid string")
        break
if len(stack) == 0:
    print("valid string")
else:
    print("invalid string")