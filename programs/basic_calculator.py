operator=str(input("choose your operator(+,-,*,/):"))
if(operator=="+"):
    a= int(input("enter first number:"))
    b= int(input("enter second number:"))
    print(a+b)
elif(operator=="-"):
    a= int(input("enter first number:"))
    b= int(input("enter second number:"))
    print(a-b)
elif(operator=="*"):
    a= int(input("enter first number:"))
    b= int(input("enter second number:"))
    print(a*b)
elif(operator=="/"):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print(a / b)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator selected.")
