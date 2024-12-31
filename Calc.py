calculations = []

def record_history(args):
    calculations.append(args)

def history():
    if calculations == []:
        print("No past calculations to show")
    else:
        for i in calculations:
            print(i)
def add(a,b):
    c=a+b
    d=f"{a}+{b}={c}"
    record_history(d)
    return c
    

def sub(a,b):
    c=a-b
    d=f"{a}-{b}={c}"
    record_history(d)
    return c
    
def mult(a,b):
    c=a*b
    d=f"{a}X{b}={c}"
    record_history(d)
    return c
    
def div(a,b):
    try:
        c=a/b
        d=f"{a}/{b}={c}"
        return c
    except:
        print("Can't be divided by 0")
        d=f"{a}/{b}={c}"
    record_history(d)

def mod(a,b):
    c=a%b
    d=f"{a}%{b}={c}"
    record_history(d)
    return c

        
while 1:
    print("Welcome to calculator")
    print('''Choose the operator which you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. History()''')
    c=int(input())
    e=int(input("Enter 1st no."))
    f=int(input("Enter 2nd no."))
    if c==1:
        d=add(e,f)
        print("Addition of two numbers is :", d)
    if c==2:
        d=sub(e,f)
        print("Subtraction of two numbers is :", d)
    if c==3:
        d=mult(e,f)
        print("Multiplication of two numbers is :", d)
    if c==4:
        d=div(e,f)
        print("Division of two numbers is :", d)
    if c==5:
        d=mod(e,f)
        print("Modulus of two numbers is :", d)
    if c==6:
        d=history()


    
