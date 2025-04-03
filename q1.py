stk=[]
top=-1
def isempty():
    global stk
    if stk==[]:
        print("stack is currently empty")
    else:
        none
def push():
    global stk
    global top
    n=int(input("enter the value to add in stack"))
    stk.append(n)
    top=len(stk)-1
    print("given value added to stack")
def display():
    global stk
    global top
    if top==-1:
        isempty()
    else:
        top=len(stk)-1
        print(stk[top],"(top value)")
        for i in range(top-1,-1,-1):
            print(stk[i])
def pop():
    global stk
    global top
    if top==-1:
        isempty()
    else:
        print("elemnt popped-->", stk.pop())
        top=top-1
def menu():
    while True:
        print('''
1. push
2. pop
3. display
4. exit
''')
        ch=int(input("what would you like to do->"))
        if ch==1:
            push()
        elif ch==2:
            pop()
        elif ch==3:
            display()
        elif ch==4:
            print("bye bitch")
            break
        else:
            print("invalid choice nigga ")
menu()