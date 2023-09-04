# factorial formula
def factorial(num):
    # num=int(input("enter number :"))
    if (num == 0 or num == 1):
        return 1
    else:
        return num*factorial(num-1)


num = int(input("enter a number :"))
print("factorial is ", factorial(num))
